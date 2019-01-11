import json
import requests
from urllib.parse import urlencode
from django.core.management.base import BaseCommand, CommandError
from museum.models import Artwork

def getJson(url):
    print('Calling '+url)
    r = requests.get(url)
    return json.loads(r.text)

class Command(BaseCommand):
    help = 'Usage: python manage.py metmuseum_highlights. See https://www.metmuseum.org/art/collection/search for details.'

    def handle(self, *args, **options):
        # get all
        params = {
            'artist': '',
            'department': '',
            'era': '',
            'geolocation': '',
            'material': 'Paintings',
            'offset': '0',
            'pageSize': '0',
            'perPage': '20',
            'searchField': 'All',
            'showOnly': 'highlights', # important!
            'sortBy': 'relevance',
            'sortOrder': 'asc',
        }
        json = getJson('https://www.metmuseum.org/api/collection/collectionlisting?'+urlencode(params))
        print('Total of '+str(json['totalResults'])+' artworks')
        for result in json['results']:
            a = Artwork(origin='metmuseum')
            a.name = result['title']
            a.url = result['image'].replace('mobile-large', 'web-large')
            a.author = result['artist']
            print(a)
