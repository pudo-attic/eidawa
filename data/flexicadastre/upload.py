import os
import json
import glob
from datetime import datetime

from googlesheets import Spreadsheet

STORE_PATH = os.path.join(os.path.dirname(__file__), 'raw')


def convrow(data):
    row = {}
    for name, val in data.items():
        if name.upper().startswith('DTE') and val is not None:
            dt = datetime.fromtimestamp(int(val)/1000)
            val = dt.date().isoformat()
        row[name] = val
    return row


def parse_file(path):
    with open(path, 'rb') as fh:
        ctx = json.load(fh)

    layers = ctx.pop('layers')
    title = 'ANCIR | Cadastre | %s' % ctx['source_title']
    ss = Spreadsheet.open(title)
    # print ss
    for layer in layers:
        if 'Mining Licence' in layer['name']:
            continue
        features = layer['data']['features']
        print [layer['name']], ss
        sheet = ss[layer['name']]
        for feature in features:
            row = convrow(feature['attributes'])
            sheet.upsert(row, ['GUIDSHAPE'])


if __name__ == '__main__':
    for file_path in glob.glob(os.path.join(STORE_PATH, 'nam*')):
        parse_file(file_path)
