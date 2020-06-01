"""
Search controller

- validate query
- handle caching
- handle actual search
"""

import sys 
sys.path.append('..')

from providers import flickr

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
        result = call(query_arguments['search'])

    return result

def call(query):
    # TODO
    print('Call query ...')
    flickrResponse = flickr.flickr_request(query)

    return flickrResponse