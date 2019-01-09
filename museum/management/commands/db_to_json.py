import json
from django.core.management.base import BaseCommand, CommandError
from museum.models import Artwork
from contextlib import suppress

headers = {'ApiKey': ''}
class Command(BaseCommand):
    def handle(self, *args, **options):
        artworks = []
        for a in Artwork.objects.all():
            artwork = a.as_dict()
            del artwork['created_datetime']
            del artwork['edited_datetime']
            artworks.append(artwork)
        f = open('docs/artworks.js', 'w')
        rawJson = json.dumps(artworks)
        f.write('var artworks = '+rawJson)
        self.stdout.write(self.style.SUCCESS('Success'))
