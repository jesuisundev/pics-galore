from pprint import pprint as pp

def build_query_strings(query):
    query_strings = ''
    first = True

    for key, value in query.items():
        delimitator = '&'

        if(first):
            first = False
            delimitator = '?'

        query_strings += "%s%s=%s" % (delimitator, key, str(value))

    return query_strings