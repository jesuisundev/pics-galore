from pprint import pprint as pp
import json
import requests
import os


def request(query):
    pp('Giphy request ...')

    url = build_url(query)

    response = requests.get(url)

    normalized_data = normalize(response)

    return normalized_data


def build_url(query):
    with open('./config/config.json') as f:
        config = json.load(f)

    if(not os.environ['GIPHY_API_KEY']):
        raise ValueError('Environement variable "GIPHY_API_KEY" is empty')
    
    current_provider = [provider for provider in config['providers'] if provider['name'] == 'giphy'][0]

    current_provider['query']['a'] = str(query)
    current_provider['query']['api_key'] = os.environ['GIPHY_API_KEY']

    base_url = current_provider['base_url']
    query_strings = build_query_strings(current_provider['query'])

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
    normalize_data = { 'source': 'giphy', 'photos': [] }
    raw_data = response.json()
    
    for photo in raw_data['data']:
        normalize_data['photos'].append({
            'name': photo['title'],
            "thumbnail": photo['images']['fixed_width_small']['url'],
            "original": photo['images']['original']['url']
        })

    return normalize_data
