"""
Search controller

- validate query
- handle caching
- handle actual search
"""

def validate_search_query(query_arguments):
    """TODO
    """
    print('Validating search query ...')
    print(query_arguments)
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
    validate_search_query(query_arguments)
    cached_data = _get_cache_by_key(query_arguments)

    if cached_data:
        print('Cache hit, return cached data ...')
        return cached_data

    return True