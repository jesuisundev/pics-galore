import json
from functools import reduce

import sys
sys.path.append('..')

from providers import provider_factory

with open('./config/config.json') as f:
    config = json.load(f)

def validate_search_query(query_arguments):
    """
    Validating the query params of the serch

    Args:
        query_arguments (dict): dictonary of params from the request

    Returns:
        [boolan]: return true if validated
    """
    if 'search' not in query_arguments:
        raise ValueError('Query search is not found in query params')

    return True


def _get_cache_by_key(key):
    """
    Try to get the cache of this request on Reids

    Args:
        key (string): key of the cache

    Returns:
        [dict|boolean]: content of the cache or false
    """
    return False


def search(query_arguments):
    """
    Try to get the cached and return it immedialty
    If no cache the call process is launch

    Args:
        query_arguments (dict): dictonary of params from the request

    Returns:
        [dict]: dictonary of content from the providers
    """
    result = False

    validate_search_query(query_arguments)
    cached_data = _get_cache_by_key(query_arguments)

    if cached_data:
        print('Cache hit, return cached data ...')
        result = cached_data
    else:
        result = _call(query_arguments['search'])
        #TODO SET CACHE

    return result


def _call(query):
    """
    Get each providers available in config throught factory and request the content

    Args:
        query (dict): dictonary of params from the request
        config (dict): dictonary of configuration

    Returns:
        [list]: list of dictonary fetched from providers
    """
    response = []
    preview = ''

    providerFactory = provider_factory.ProviderFactory()
    
    for provider in config['providers']:
        current_provider = providerFactory.create(provider['name'])
        provider_response = current_provider.request(config, query)
        response.append(provider_response)
        preview += _preview_html(provider_response)

    return preview


def _preview_html(response):
    """
    Temporary function to transform the list result into html
    """
    preview_html = ''
    for photo in response['photos']:
        preview_html += '<img src="%s" alt="" />' % photo['original']

    return preview_html