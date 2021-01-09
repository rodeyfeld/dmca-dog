import requests
from bs4 import BeautifulSoup


class LumenAPI:
    base_url: str = "https://lumendatabase.org/notices/search"

    def fetch(self, query: str) -> str:
        params = {
            'utf8': '✓',
            'country_code_facet': 'US',
            'term': query,
        }
        headers = {
            'User-agent': 'my_bot',
        }
        response = requests.get(self.base_url, params=params, headers=headers)
        return response.text

    @staticmethod
    def get_content(response_text):
        soup = BeautifulSoup(response_text, 'html.parser')
        try:
            return soup.find('span', class_='total-entries').get_text()
        except AttributeError:
            return "Failed to get results"

    def process(self, query):
        response_text = self.fetch(query)
        content = self.get_content(response_text)
        return content
