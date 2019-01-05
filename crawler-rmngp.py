#!/usr/bin/env python3
import requests
import json
import yaml
from contextlib import suppress
config = yaml.safe_load(open("config.yml"))

headers = {'ApiKey': config['rmngp']['api_key']}
r = requests.get('https://api.art.rmngp.fr/v1/works?page=2', headers=headers)
artworks = json.loads(r.text)['hits']['hits']

for artwork in artworks:
    o = {}
    a = artwork['_source']
    with suppress (KeyError, IndexError):
        o['title'] = a['title']['fr']
    with suppress (KeyError, IndexError):
        o['author'] = a['authors'][0]['name']['fr']
    with suppress (KeyError, IndexError):
        o['href'] = a['images'][0]['urls']['original']
    print(o)
