import requests
import json
from config import *

headers = {'ApiKey': RMNGP_API_KEY}
def getRmngpObject(resource):
    url = 'https://api.art.rmngp.fr/v1/'+resource.replace(' ', '%20')
    print('Calling '+url)
    return json.loads(requests.get(url, headers=headers).text)
