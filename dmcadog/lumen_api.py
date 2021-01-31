import os

import requests
from bs4 import BeautifulSoup


class LumenAPI:
    """
     A class for querying the Lumen DMCA database. Uses Beautiful Soup to
     parse results.
    """

    def __init__(self):
        self.base_url: str = "https://lumendatabase.org/notices/search"
        self.bot_name: str = os.environ.get("BOT_NAME")

    def fetch(self, query: str) -> str:
        """
        Connects to Lumen page and fetches HTML
        :param query: string that will be lookup up in Lumen
        :return: string with all HTML text
        """
        params = {
            'utf8': '✓',
            'country_code_facet': 'US',
            'title': query,
            'term-require-all': "true"
        }
        headers = {
            'User-Agent': f"{self.bot_name}"
        }
        response = requests.get(self.base_url, params=params, headers=headers)
        return response.text

    @staticmethod
    def get_content(response_text):
        """
        Beautiful soup parser for HTML
        :param response_text: HTML string containing Lumen data
        :return: String containing total number of results
        """
        soup = BeautifulSoup(response_text, 'html.parser')
        try:
            return soup.find('span', class_='total-entries').get_text()
        except AttributeError:
            return "Failed to get results"

    def process(self, query):
        """
        Primary access route for API requests
        :param query: string that will be lookup up in Lumen
        :return: string containing results
        """
        response_text = self.fetch(query)
        content = self.get_content(response_text)
        return content
