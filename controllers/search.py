import threading
import time
import json
import redis
cache = redis.Redis(host='redis', port=6379)

import logging
logging.basicConfig(format="%(asctime)s: %(message)s", level=logging.INFO, datefmt="%H:%M:%S")

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
    cached_data = cache.get(query_arguments['search'])

    if cached_data:
        print('Cache hit, return cached data ...')
        result = cached_data
    else:
        print('Cache miss, fetch data ...')
        result = _call(query_arguments['search'])
        cache.set(query_arguments['search'], result)

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
    
    logging.info("Search %s: starting")

    for provider in config['providers']:
        current_provider = providerFactory.create(provider['name'])
        provider_response = current_provider.request(config, query)
        response.append(provider_response)
        preview += _preview_html(provider_response)

    logging.info("Search %s: finishing")

    return preview


def _preview_html(response):
    """
    Temporary function to transform the list result into html
    """
    preview_html = ''
    for photo in response['photos']:
        preview_html += '<img src="%s" alt="" />' % photo['original']

    return preview_html