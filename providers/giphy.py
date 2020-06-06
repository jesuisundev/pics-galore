from pprint import pprint as pp
import json
import requests
import os

class Giphy:


    def __init__(self, config, query):
        self.config = config
        self.query = query


    def request(self):
        pp('Giphy request ...')

        response = requests.get(self.build_url())

        normalized_data = self.normalize(response)

        return normalized_data


    def build_url(self):
        if(not os.environ['GIPHY_API_KEY']):
            raise ValueError('Environement variable "GIPHY_API_KEY" is empty')
        
        current_provider = [provider for provider in self.config['providers'] if provider['name'] == 'giphy'][0]

        current_provider['query']['q'] = str(self.query)
        current_provider['query']['api_key'] = os.environ['GIPHY_API_KEY']

        base_url = current_provider['base_url']
        query_strings = self._build_query_strings(current_provider)

        return base_url + query_strings


    def _build_query_strings(self, current_provider):
        query_strings = ''
        first = True

        for key, value in current_provider['query'].items():
            delimitator = '&'

            if(first):
                first = False
                delimitator = '?'

            query_strings += "%s%s=%s" % (delimitator, key, str(value))

        return query_strings


    def normalize(self, response):
        normalize_data = { 'source': 'giphy', 'photos': [] }
        raw_data = response.json()
        
        for photo in raw_data['data']:
            normalize_data['photos'].append({
                'name': photo['title'],
                "thumbnail": photo['images']['fixed_width_small']['url'],
                "original": photo['images']['original']['url']
            })

        return normalize_data
