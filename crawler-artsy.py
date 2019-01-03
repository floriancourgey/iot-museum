#!/usr/bin/env python3
import requests
import json
import random

headers = {'X-Xapp-Token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyb2xlcyI6IiIsImV4cCI6MTU0Njk2OTUzNiwiaWF0IjoxNTQ2MzY0NzM2LCJhdWQiOiI1YzJiYTc0MGNkNjA5MTVkNjU4YzgyY2IiLCJpc3MiOiJHcmF2aXR5IiwianRpIjoiNWMyYmE3NDA1MTIyNGIzNGUyYTA0N2IyIn0.SzQFRFIam0XpVVZ5SkUFcoG5iek1YwOGuTThl-1_EBA'}
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
