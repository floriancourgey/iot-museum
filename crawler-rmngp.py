#!/usr/bin/env python3
import requests
import json
import time
from config import config
from sqlalchemy import create_engine
from contextlib import suppress
from flask import Flask, render_template
from models import db, Artwork

headers = {'ApiKey': config['rmngp']['api_key']}
for i in range(31,40):
    print('Page '+str(i))
    r = requests.get('https://api.art.rmngp.fr/v1/works?page='+str(i), headers=headers)
    artworks = json.loads(r.text)['hits']['hits']

    for artwork in artworks:
        o = Artwork()#origin='rmngp')
        a = artwork['_source']
        with suppress (KeyError, IndexError):
            o.name = a['title']['fr']
        with suppress (KeyError, IndexError):
            o.author = a['authors'][0]['name']['fr']
        with suppress (KeyError, IndexError):
            o.url = a['images'][0]['urls']['original']
        if not o.name or not o.url:
            continue
        print(o)
        existing = db.session.query(Artwork).filter(Artwork.url==o.url).first()
        if not existing:
            db.session.add(o)
    db.session.commit()
    print('Page '+str(i)+' done')
    time.sleep(0.5)

query = db.session.query(Artwork).all()
for artwork in query:
    print(artwork.name, artwork.id)
