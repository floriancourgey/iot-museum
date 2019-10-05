from django.core.management.base import BaseCommand, CommandError
from crawler_rijks.management.commands._functions import rijksSearch

# http://rijksmuseum.github.io/#collection

class Command(BaseCommand):
    help = 'Usage: python manage.py rmngp_search "gogh"'

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('query')
    def handle(self, *args, **options):
        print('Searching "'+options['query']+'"...')
        result = rijksSearch(options['query'])
        count = result['count']
        if count < 1:
            print('No artwork found')
            return
        print(str(count)+' artworks found, showing 10 most probable:')
        for artwork in result['artObjects']:
            print('- '+artwork['title'])
