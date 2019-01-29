import requests
import json
from config import config

headers = {'ApiKey': config['rmngp']['api_key']}
def getRmngpObject(resource):
    url = 'https://api.art.rmngp.fr/v1/'+resource.replace(' ', '%20')
    print('Calling '+url)
    obj = json.loads(requests.get(url, headers=headers).text)
    if 'error' in obj:
        raise Exception('RmnGP API error:', obj['error'])
    return obj
