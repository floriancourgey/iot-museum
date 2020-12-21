from django.db.models import Q
from django.core.management.base import BaseCommand, CommandError
from museum.models import Artwork, Origin
from contextlib import suppress
from crawler_rmngp.management.commands.functions import getRmngpObject

class Command(BaseCommand):
    help = 'Usage: python manage.py rmngp_works'

    def add_arguments(self, parser):
        parser.add_argument('--author')
        parser.add_argument('--per_page', type=int, default=15,
            help='integer for the "per_page" api parameter')
        parser.add_argument('--page', type=int, default=1,
            help='integer for the "page" api parameter')

    def handle(self, *args, **options):
        url = 'works?'
        url += 'per_page='+str(options['per_page'])+'&'
        url += 'page='+str(options['page'])+'&'

        if options['author']:
            url += 'facets[authors]='+options['author']

        result = getRmngpObject(url)
        if result['hits']['total'] < 1:
            print('No results')
            return

        # convert json to Artwork objects
        print('Got API result, parsing...')
        artworks = []
        origin = Origin.objects.get(id='rmngp')
        for artwork in result['hits']['hits']:
            if artwork['_score'] < 1:
                continue
            a = Artwork(origin=origin)
            json = artwork['_source']
            # mandatory fields
            with suppress (KeyError, IndexError):
                a.name = json['title']['fr']
            with suppress (KeyError, IndexError):
                a.url_online = json['images'][0]['urls']['original']
            if not a.name or not a.url_online:
                continue
            # check existing: artwork with same url or same name
            existing = Artwork.objects.filter(
                Q(url_online=a.url_online) | Q(name=a.name)
            ).first()
            # if existing, we update it
            if existing:
                a = existing
            # other fields
            with suppress (KeyError, IndexError):
                a.author = json['authors'][0]['name']['fr']
            with suppress (KeyError, IndexError):
                a.date_display = json['date']['display']
                a.date_display = a.date_display.replace('T00:00:00+00:00', '') # RmnGP sometimes adds timestamp
            with suppress (KeyError, IndexError):
                a.origin_artwork_id = json['id']
            # append it to master
            artworks.append(a)

        if len(artworks) < 1:
            print('No artwork to add')
            return

        # recap
        print('Adding '+str(len(artworks))+' artworks:')
        for a in artworks:
            text = '- '+str(a)
            if a.id and a.id > 0:
                text += ' -> UPDATE'
            print(text)

        # ask to add to db
        s = input('Add to database [y/N]? ')
        if s != 'y':
            exit()

        for a in artworks:
            a.save()
        print(str(len(artworks))+' artworks have successfully been added to the database.')
