import json
import requests
import os
import sys
sys.path.append('../modules/')

from modules import helper

class Giphy:

    def __init__(self):
        self.provider_name = 'giphy'


    def request(self, config, query):
        """
        Make a HTTP request on provider and normalize the data

        Returns:
            [dict]: dictonary of images from this provider
        """
        url = self.build_url(config, query)
        response = requests.get(url)
        normalized_data = self.normalize(response)

        return normalized_data


    def build_url(self, config, query):
        """
        Build the search url for the current provider using the config

        Raises:
            ValueError: should raise a error with api key

        Returns:
            [string]: full url for the request
        """
        if(not os.environ['GIPHY_API_KEY']):
            raise ValueError('Environement variable "GIPHY_API_KEY" is empty')
        
        current_provider = [provider for provider in config['providers'] if provider['name'] == self.provider_name][0]
        current_provider['query']['q'] = str(query)
        current_provider['query']['api_key'] = os.environ['GIPHY_API_KEY']

        query_strings = helper.build_query_strings(current_provider['query'])

        return current_provider['base_url'] + query_strings


    def normalize(self, response):
        """
        Normalizing the data received from the provider

        Args:
            response ([requests.models.Response]): data from provider

        Returns:
            [dict]: normalized dictonary
        """
        normalize_data = { 'source': self.provider_name, 'photos': [] }
        raw_data = response.json()
        
        for photo in raw_data['data']:
            normalize_data['photos'].append({
                'name': photo['title'],
                "thumbnail": photo['images']['fixed_width_small']['url'],
                "original": photo['images']['original']['url']
            })

        return normalize_data
