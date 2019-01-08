#!/usr/bin/env python3
import requests
import json
import random
from config import config
from models import db, Artwork
from contextlib import suppress

headers = {'X-Xapp-Token': config['artsy']['x_xapp_token']}
def getArtsyObject(url):
    return json.loads(requests.get(url, headers=headers).text)

nextUrl = 'https://api.artsy.net/api/artworks?size=50&offset=15'
artists = {} # store artists name
for i in range(0,1):
    print('Next url:', nextUrl)
    response = getArtsyObject(nextUrl)
    artworks = response['_embedded']['artworks']
    for a in artworks:
        o = Artwork()#origin='artsy')
        with suppress (KeyError, IndexError):
            o.name = a['title']
        # get author via API call (or cache)
        with suppress (KeyError, IndexError):
            href = a['_links']['artists']['href']
            if not href in artists:
                artist = getArtsyObject(href)
                artists[href] = artist['_embedded']['artists'][0]['name']
            o.author = artists[href]
        with suppress (KeyError, IndexError):
            href = a['_links']['image']['href']
            if 'large' in a['image_versions']:
                href = href.replace('{image_version}', 'large')
            else:
                href = href.replace('{image_version}', a['image_versions'][0])
            o.url = href
        if not o.name or not o.url:
            continue
        print(o)
        existing = db.session.query(Artwork).filter(Artwork.url==o.url).first()
        if not existing:
            db.session.add(o)
    db.session.commit()
    # next
    nextUrl = response['_links']['next']['href']
