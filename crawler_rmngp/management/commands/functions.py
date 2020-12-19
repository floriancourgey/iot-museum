import os
import requests
import json

headers = {'ApiKey': os.getenv('RMNGP_API_KEY')}
def getRmngpObject(resource):
    url = 'https://api.art.rmngp.fr/v1/'+resource.replace(' ', '%20')
    print('Calling '+url)
    obj = json.loads(requests.get(url, headers=headers).text)
    if 'error' in obj:
        raise Exception('RmnGP API error:', obj['error'])
    return obj
