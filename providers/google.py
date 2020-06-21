import json
import requests
from bs4 import BeautifulSoup
import os

from modules import helper

class Google():

    def __init__(self):
        self.provider_name = 'google'


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
        current_provider = [provider for provider in config['providers'] if provider['name'] == self.provider_name][0]
        current_provider['query']['q'] = str(query)

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

        soup = BeautifulSoup(response.content, 'html.parser')

        links = soup.find_all("a")

        for link in links:
            imgByLink = link.find_all('img')

            if imgByLink and imgByLink[0].get('alt') != 'Google logo':
                normalize_data['photos'].append({
                    'name': 'title',
                    "thumbnail": imgByLink[0].get('src'),
                    "original": link.get('href').replace('/url?q=', '')
                })

        return normalize_data