import time
import requests
import json
from django.core.management.base import BaseCommand, CommandError
from museum.models import Artwork
from contextlib import suppress

headers = {'ApiKey': ''}
class Command(BaseCommand):
    def handle(self, *args, **options):
        for i in range(1,2):
            print('Page '+str(i))
            r = requests.get('https://api.art.rmngp.fr/v1/works?page='+str(i), headers=headers)
            artworks = json.loads(r.text)['hits']['hits']

            for artwork in artworks:
                o = Artwork(origin='rmngp')
                a = artwork['_source']
                with suppress (KeyError, IndexError):
                    o.name = a['title']['fr']
                with suppress (KeyError, IndexError):
                    o.author = a['authors'][0]['name']['fr']
                with suppress (KeyError, IndexError):
                    o.url = a['images'][0]['urls']['original']
                if not o.name or not o.url:
                    continue
                existing = Artwork.objects.filter(url=o.url)
                if not existing:
                    o.save()
            print('Page '+str(i)+' done')
            time.sleep(0.5)

        self.stdout.write(self.style.SUCCESS('Success'))
