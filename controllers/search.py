"""
Search controller

- validate query
- handle caching
- handle actual search
"""

import json
import sys
sys.path.append('..')

from providers import flickr, giphy

with open('./config/config.json') as f:
    config = json.load(f)


def validate_search_query(query_arguments):
    """TODO
    """

    print('Validating search query ...')

    if 'search' not in query_arguments:
        raise ValueError('Query search is not found in query params')

    return True


def _get_cache_by_key(key):
    """TODO

    Arguments:
        key {[type]} -- [description]
    """
    print('Get cache by key ...')
    return False


def search(query_arguments):
    # TODO
    result = False

    validate_search_query(query_arguments)
    cached_data = _get_cache_by_key(query_arguments)

    if cached_data:
        print('Cache hit, return cached data ...')
        result = cached_data
    else:
        result = _call(config, query_arguments['search'])

    return result


def _call(query, config):
    # TODO
    print('Call query ...')
    response = []
    preview = ''

    for provider in flickr.Flickr(query, config), giphy.Giphy(query, config):
        provider_response = provider.request()
        response.append(provider_response)
        preview += _preview_html(provider_response)

    return preview


def _preview_html(response):
    preview_html = ''
    for photo in response['photos']:
        preview_html += '<img src="%s" alt="" />' % photo['original']

    return preview_html