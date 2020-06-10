def build_query_strings(query):
    """
    Building the query strings from the configuration

    Args:
        query ([dict]): dictonary of configuration

    Returns:
        [string]: querystrings built
    """
    query_strings = ''
    first = True

    for key, value in query.items():
        delimitator = '&'

        if(first):
            first = False
            delimitator = '?'

        query_strings += "%s%s=%s" % (delimitator, key, str(value))

    return query_strings