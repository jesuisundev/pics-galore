from pprint import pprint as pp

import requests


def flickr_request(query):
    pp('Flickr request ...')

    url = build_url(query)

    response = requests.get(url)

    normalized_data = normalize(response)

    return normalized_data


def build_url(query):
    base_url = 'https://www.flickr.com/services/rest/'
    service = 'flickr.photos.search'
    key = ''
    url = base_url + '?method=' + service + '&api_key=' + key + '&text=' + query + '&safe_search=3&format=json&nojsoncallback=true'

    return url


def normalize(response):
    normalize_data = []
    raw_data = response.json()
    
    for photo in raw_data['photos']['photo']:
        current_photo = _build_photos_url(photo)
        normalize_data.append({
            'name': photo['title'],
            'photos': {
                "thumbnail": current_photo['thumbnail'],
                "original": current_photo['original']
            },
            'source': 'Flickr'
        })

    return normalize_data


def _build_photos_url(photo):
    extension = '.jpg'
    base_url = 'https://farm%s.staticflickr.com/%s/%s_%s' % (
        photo['farm'],
        photo['server'],
        photo['id'],
        photo['secret']
    )

    return {
        'thumbnail': base_url + '_t' + extension,
        'original': base_url + extension
    }