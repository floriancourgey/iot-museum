#!/usr/bin/env python3
import requests
import json
import random
import yaml
config = yaml.safe_load(open("config.yml"))

headers = {'X-Xapp-Token': config['artsy']['x_xapp_token']}
r = requests.get('https://api.artsy.net/api/artworks', headers=headers)
idx = range(random.randint(1,5))
print('Rand:', idx)
for i in idx:
    next = json.loads(r.text)['_links']['next']['href']
    print('New url:', next)
    r = requests.get(next, headers=headers)
artworks = json.loads(r.text)['_embedded']['artworks']
html = ''
for artwork in artworks:
    html += '<h2>'+artwork['title']+'</h2>'
    href = artwork['_links']['image']['href']
    href = href.replace('{image_version}', 'medium')
    html += '<img src="'+href+'"><br>'
