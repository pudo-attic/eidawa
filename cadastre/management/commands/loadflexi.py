import unicodecsv

from django.core.management.base import BaseCommand

from cadastre.models import License, LicenseHolder, Commodity
from cadastre.models import Company, CompanyPlaceholder

COMS = set()


class Command(BaseCommand):
    args = '<csv_file csv_file ...>'
    help = 'Import a set of CSV files extracted from FlexiCadastre'

    def handle(self, *args, **options):
        for csv_file in args:
            load_csv(csv_file)
            # safe_name = csv_file.decode('utf-8')
            # self.stdout.write('Successfully imported "%s"' % safe_name)
        print '\n'.join(sorted([d for d in COMS]))


def clean_text(text):
    if text is None:
        return
    return text.strip()


def parse_date(text):
    from dateutil.parser import parse
    if text is None or len(text) == 0:
        return None
    return parse(text)


def parse_area(text, factor=1):
    try:
        area = float(text)
        return area * factor
    except (ValueError, TypeError):
        return None


def parse_commodities(texts):
    commodities = set()
    for text in texts:
        if text is None:
            continue
        cds = text.split(', ')
        for c in cds:
            c = c.replace(' (applied for)', '')
            c = c.strip()
            if len(c):
                commodities.add(c)

    # print commodities
    # COMS.update(commodities)
    return commodities


def parse_parties(text):
    import re
    if text is None or not len(text.strip()):
        return []
    text = clean_text(text)
    pct_re = re.compile(r'\(([0-9\., ]*)%?\)')
    match = pct_re.search(text)
    interest = 100.0
    if match is not None:
        text = pct_re.sub('', text).strip()
        try:
            interest = float(match.group(1))
        except:
            pass
    return [(text, interest)]


def load_csv(file):
    with open(file, 'rb') as fh:
        for row in unicodecsv.DictReader(fh):
            load_row(row)

FOO = set()
PAR = set()


def load_row(row):
    identifier = row.get('CONCESSION') or row.get('NAME') or \
        row.get('CODE') or row.get('OBJECTID')
    identifier = clean_text(identifier)
    country = row.get('source_name')

    for k, v in row.items():
        if k not in FOO:
            #print (k, v)
            FOO.add(k)

    #if country == 'MZ':
    #    return

    #parties, interest = 
    #return

    qs = License.objects.filter(identifier=identifier).filter(country=country)
    if len(qs):
        license = qs[0]
    else:
        license = License(identifier=identifier, country=country)

    license.source_label = row.get('source_title')
    license.source_url = row.get('source_url')

    area = parse_area(row.get('AREA')) or \
        parse_area(row.get('AREAVALUE')) or \
        parse_area(row.get('AREA_KM'), 100)
    license.area = area

    license.date_applied = parse_date(row.get('DTEAPPLIED') or row.get('DTESTART'))
    license.date_granted = parse_date(row.get('DTEGRANTED') or row.get('DTESIGNED'))
    license.date_expires = parse_date(row.get('DTEEXPIRES') or row.get('DTEEND'))
    license.date_renewal = parse_date(row.get('DTERENEWAL'))
    license.date_pegged = parse_date(row.get('DTEPEGGED'))

    license.save()

    for company, interest in parse_parties(row.get('PARTIES')):
        qs = CompanyPlaceholder.objects.filter(label=company)
        qs = qs.filter(jurisdiction=country)
        if len(qs):
            ph = qs[0]
            if ph.company is None:
                com = Company(label=company, jurisdiction=country)
                com.source_label = row.get('source_title')
                com.source_url = row.get('source_url')
                com.save()
                ph.company = com
                ph.save()

        else:
            com = Company(label=company, jurisdiction=country)
            com.source_label = row.get('source_title')
            com.source_url = row.get('source_url')
            com.save()
            ph = CompanyPlaceholder(label=company, jurisdiction=country)
            ph.source_label = row.get('source_title')
            ph.source_url = row.get('source_url')
            ph.company = com
            ph.save()

        found = False
        for holder in license.holders.all():
            if holder.company_placeholder == ph:
                holder.interest = interest
                found = True
        if not found:
            lh = LicenseHolder(license=license, company_placeholder=ph,
                               interest=interest)
            lh.source_label = row.get('source_title')
            lh.source_url = row.get('source_url')
            lh.save()
        # print (company, country, interest)

    # commodities = (row.get('RESOURCES'), row.get('RESOURCESCD'),
    #                row.get('COMMODITIES'), row.get('COMMODITIESCD'))
    # commodities = parse_commodities(commodities)

    
