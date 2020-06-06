from pprint import pprint as pp
import json
import requests
import os

class Flickr:


    def __init__(self, config, query):
        self.config = config
        self.query = query


    def request(self):
        pp('Flickr request ...')

        response = requests.get(self.build_url())

        normalized_data = self.normalize(response)

        return normalized_data


    def build_url(self):
        if(not os.environ['FLICKR_API_KEY']):
            raise ValueError('Environement variable "FLICKR_API_KEY" is empty')
        
        
        current_provider = [provider for provider in self.config['providers'] if provider['name'] == 'flickr'][0]
        
        current_provider['query']['text'] = str(self.query)
        current_provider['query']['api_key'] = os.environ['FLICKR_API_KEY']

        base_url = current_provider['base_url']
        query_strings = self._build_query_strings(current_provider)

        return base_url + query_strings


    def normalize(self, response):
        normalize_data = { 'source': 'Flickr', 'photos': [] }
        raw_data = response.json()
        
        for photo in raw_data['photos']['photo']:
            current_photo = self._build_photos_url(photo)
            normalize_data['photos'].append({
                'name': photo['title'],
                "thumbnail": current_photo['thumbnail'],
                "original": current_photo['original']
            })

        return normalize_data


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


    def _build_photos_url(self, photo):
        extension = '.jpg'
        base_url = 'https://farm%s.staticflickr.com/%s/%s_%s' % (
            photo['farm'],
            photo['server'],
            photo['id'],
            photo['secret']
        )

        return {
            'thumbnail': base_url + '_t' + extension,
            'original': base_url + extension
        }