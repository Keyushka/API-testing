import os
import requests
from dotenv import load_dotenv

load_dotenv()

class Session(requests.Session):
    base_url = os.getenv('BASE_URL')

    def request(self, method, url, *args, **kwargs):
        if self.base_url:
            url = self.base_url + url
        headers = kwargs.get('headers', {})
        headers['Authorization'] = os.getenv("TOKEN")
        kwargs['headers'] = headers
        return super().request(method, url, *args, **kwargs)
