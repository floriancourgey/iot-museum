import os
import requests
import json

locale = 'en'
api_key = os.getenv('RIJKS_API_KEY')
def rijksSearch(resource):
    url = 'https://www.rijksmuseum.nl/api/'+locale+'/collection?key='+api_key+'&format=json&q='+resource.replace(' ', '%20')
    print('Calling '+url)
    obj = json.loads(requests.get(url).text)
    if 'error' in obj:
        raise Exception('Rijks API error:', obj['error'])
    return obj
