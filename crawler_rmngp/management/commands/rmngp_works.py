from django.db.models import Q
from django.core.management.base import BaseCommand, CommandError
from museum.models import Artwork
from contextlib import suppress
from crawler_rmngp.management.commands.functions import getRmngpObject

MAX_PER_PAGE = 15

class Command(BaseCommand):
    help = 'Usage: python manage.py rmngp_works --author "Vincent Van Gogh"'

    def add_arguments(self, parser):
        parser.add_argument('--author')

    def handle(self, *args, **options):
        url = 'works?per_page='+str(MAX_PER_PAGE)+'&'
        if options['author']:
            url += 'facets[authors]='+options['author']

        result = getRmngpObject(url)
        if result['hits']['total'] < 1:
            print('No results')
            return

        # convert json to Artwork objects
        artworks = []
        for artwork in result['hits']['hits']:
            if artwork['_score'] < 1:
                continue
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
            # look for an artwork with same url or same name
            existing = Artwork.objects.filter(
                Q(url=o.url) | Q(name=o.name)
            )
            if not existing:
                artworks.append(o)

        if len(artworks) < 1:
            print('No artwork to add')
            return

        # recap
        print('Adding '+str(len(artworks))+' artworks:')
        for a in artworks:
            print('- '+str(a))

        # ask to add to db
        s = input('Add to database [y/n]? ')
        if s == 'y':
            for a in artworks:
                a.save()
        print(str(len(artworks))+' artworks have been successfully added to the database.')
