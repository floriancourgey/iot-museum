#!/usr/bin/env python3
import requests
import json
import yaml
config = yaml.safe_load(open("config.yml"))

headers = {'ApiKey': config['rmngp']['api_key']}
r = requests.get('https://api.art.rmngp.fr/v1/works?page=2', headers=headers)
artworks = json.loads(r.text)['hits']['hits']

for artwork in artworks:
    o = {}
    a = artwork['_source']
    try:
        o['title'] = a['title']['fr']
    except (KeyError, IndexError):
        pass
    try:
        o['author'] = a['authors'][0]['name']['fr']
    except (KeyError, IndexError):
        pass
    try:
        o['href'] = a['images'][0]['urls']['original']
    except (KeyError, IndexError):
        pass
    print(o)
