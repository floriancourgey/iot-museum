import json
import requests
import yaml
import os
from django.core.management.base import BaseCommand, CommandError

cacheFilename = os.path.dirname(os.path.realpath(__file__))+'/cache.yml'
cacheFile = open(cacheFilename, 'a+') # a+ to create if not existing
cacheFile.seek(0, 0)
cache = yaml.load(cacheFile) or {'minId':0, 'highlightedArtworksIds':[]}
cacheFile.close()

def saveCache():
    cacheFile = open(cacheFilename, 'w')
    yaml.dump(cache, cacheFile)
    cacheFile.close()

def getJson(url):
    print('Calling '+url)
    r = requests.get(url)
    return json.loads(r.text)

class Command(BaseCommand):
    help = 'Usage: python manage.py metmuseum_objects. See https://metmuseum.github.io/ for details.'

    def handle(self, *args, **options):
        # get all
        result = getJson('https://collectionapi.metmuseum.org/public/collection/v1/objects')
        print('Found '+str(result['total'])+' objects')
        objectIDs = result['objectIDs']
        print('URL response OK')
        i = 0
        for id in objectIDs:
            if id < cache['minId']:
                continue
            cache['minId'] = id
            saveCache()
            # get details
            object = getJson('https://collectionapi.metmuseum.org/public/collection/v1/objects/'+str(id))
            if not object['isHighlight']:
                continue
            cache['highlightedArtworksIds'].append({
                'objectID': object['objectID'],
                'title': object['title'],
                'artistDisplayName': object['artistDisplayName'],
                'objectDate': object['objectDate'],
            })
            saveCache()
            i += 1
            print('===========')
            print(i, object['title'])
            print(object)
            print('===========')
            if i >= 10:
                exit()
