import json
import requests
from django.core.management.base import BaseCommand, CommandError

def getJson(url):
    print('Calling '+url)
    r = requests.get(url)
    return json.loads(r.text)

class Command(BaseCommand):
    help = 'Usage: python manage.py metmuseum_objects'

    def handle(self, *args, **options):
        minId = 40000
        result = getJson('https://collectionapi.metmuseum.org/public/collection/v1/objects')
        print('Found '+str(result['total'])+' objects')
        objectIDs = result['objectIDs']
        print('URL response OK')
        i = 0
        for id in objectIDs:
            if id < minId:
                continue
            object = getJson('https://collectionapi.metmuseum.org/public/collection/v1/objects/'+str(id))
            # print(object)
            if not object['isHighlight']:
                continue
            i += 1
            print(i, object['title'])
            if i >= 10:
                exit()
