"""
Main app entry
Define the api and delegate all process to modules
"""

import sys
sys.path.append('controllers/')

from controllers import search
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def homepage():
    """homepage => should be the VueJS UI

    Returns:
        {string} -- TODO
    """
    return 'Welcome to Pics Galore'


@app.route('/search', methods=['GET'])
def _search():
    """launch the search on each provider

    Returns:
        [type] -- [description]
    """
    result = search.search(dict(request.args))
    return str(result)