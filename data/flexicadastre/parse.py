# coding: utf-8
import os
import json
import glob
import dataset
from datetime import datetime
from pprint import pprint

SOURCE_PATH = os.path.join(os.path.dirname(__file__), 'raw')
DEST_PATH = os.path.join(os.path.dirname(__file__), 'csv')

IGNORE_LAYERS = ['Farms', 'Region', 'Districts',
                 'Withdrawn Areas', 'Divisions',
                 'Environmentally Sensitive Areas',
                 u'Áreas de Conservação - Buffer',
                 u'Áreas de Conservação',
                 u'Áreas Reservadas']


def convrow(data):
    row = {}
    for name, val in data.items():
        name = name.upper()
        if name.startswith('DTE') and val is not None:
            dt = datetime.fromtimestamp(int(val) / 1000)
            val = dt.date().isoformat()
        if name.startswith('GUID'):
            continue
        if name == 'ID':
            name = 'FC_ID'
        row[name] = val
    return row


def parse_file(path):
    with open(path, 'rb') as fh:
        ctx = json.load(fh)

    if ctx['source_name'] not in ['NA', 'MZ']:
        return

    layers = ctx.pop('layers')
    for layer in layers:
        if layer['name'] in IGNORE_LAYERS:
            continue
        eng = dataset.connect('sqlite://')
        tbl = eng['all']

        lctx = ctx.copy()
        lctx['layer_name'] = layer['name']
        lctx['layer_id'] = layer['id']
        del lctx['rest_url']

        features = layer['data']['features']
        print ctx['source_url'], layer['name'], layer['id'], len(features)

        for feature in features:
            attrs = convrow(feature.get('attributes'))
            attrs.update(lctx)
            tbl.insert(attrs)

        fn = '%(source_name)s-%(layer_id)s %(layer_name)s.csv' % lctx
        dataset.freeze(tbl, filename=fn, format='csv', prefix=DEST_PATH)


if __name__ == '__main__':
    for file_path in glob.glob(os.path.join(SOURCE_PATH, '*')):
        parse_file(file_path)
