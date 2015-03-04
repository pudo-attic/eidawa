import unicodecsv

from django.core.management.base import BaseCommand

from cadastre.models import License, LicenseHolder, Commodity


class Command(BaseCommand):
    args = '<csv_file csv_file ...>'
    help = 'Import a set of CSV files extracted from FlexiCadastre'

    def handle(self, *args, **options):
        for csv_file in args:
            load_csv(csv_file)
            safe_name = csv_file.decode('utf-8')
            self.stdout.write('Successfully imported "%s"' % safe_name)


def clean_text(text):
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


def load_csv(file):
    with open(file, 'rb') as fh:
        for row in unicodecsv.DictReader(fh):
            load_row(row)


def load_row(row):
    identifier = row.get('NAME') or row.get('CODE') or row.get('OBJECTID')
    identifier = clean_text(identifier)
    country = row.get('source_name')

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
