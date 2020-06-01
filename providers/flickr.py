from pprint import pprint as pp

import requests

def flickr_request(query):
    pp('Flickr request ...')
    base_url = 'https://www.flickr.com/services/rest/'
    service = 'flickr.photos.search'
    key = ''
    url = base_url + '?method=' + service + '&api_key=' + key + '&text=' + query + '&safe_search=3&format=json&nojsoncallback=true'

    response = requests.get(url)

    normalized_data = normalize(response)

    return response.text


def normalize(response):
    pp(response)
    pp(response.json())

    ## next up =>https://www.flickr.com/services/api/misc.urls.html

    return 'test'