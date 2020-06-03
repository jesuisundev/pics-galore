from pprint import pprint as pp
import json
import requests


def flickr_request(query):
    pp('Flickr request ...')

    url = build_url(query)

    response = requests.get(url)

    normalized_data = normalize(response)

    return normalized_data


def build_url(query):
    with open('./config/config.json') as f:
        config = json.load(f)

    config['providers']['flickr']['query']['text'] = str(query)
    base_url = config['providers']['flickr']['base_url']
    query_strings = build_query_strings(config['providers']['flickr']['query'])

    return base_url + query_strings


def build_query_strings(config):
    query_strings = ''
    first = True

    for key, value in config.items():
        delimitator = '&'

        if(first):
            first = False
            delimitator = '?'

        query_strings += "%s%s=%s" % (delimitator, key, str(value))

    return query_strings


def normalize(response):
    normalize_data = { 'source': 'Flickr', 'photos': [] }
    raw_data = response.json()
    
    for photo in raw_data['photos']['photo']:
        current_photo = _build_photos_url(photo)
        normalize_data['photos'].append({
            'name': photo['title'],
            "thumbnail": current_photo['thumbnail'],
            "original": current_photo['original']
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