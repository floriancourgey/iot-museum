from django.core.management.base import BaseCommand, CommandError
from crawler_rmngp.management.commands.functions import getRmngpObject

class Command(BaseCommand):
    help = 'Usage: python manage.py rmngp_search_author "gogh"'

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('author_name')
    def handle(self, *args, **options):
        print('Searching "'+options['author_name']+'"...')
        result = getRmngpObject('authors?q='+options['author_name'])
        count = result['hits']['total']
        if count < 1:
            print('No author found')
            return
        print(str(count)+' authors found, showing 10 most probable:')
        for author in result['hits']['hits']:
            print('- '+author['_source']['name']['fr']+' (Score '+str(int(author['_score']))+')')
