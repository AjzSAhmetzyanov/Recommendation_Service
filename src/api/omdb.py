import requests
from typing import Optional, List


class OMDBApi:

    def __init__(self, api_key):
        self.api_key = api_key
        self.url = "https://www.omdbapi.com"

    def _images_path(self, title: str) -> Optional[str]:
        params = {
            "apikey": self.api_key,
            "t": title,
            }

        response = requests.get(self.url, params=params)
        data = response.json()

        if data.get("Response") == "True":
            poster_url = data.get("Poster")
            if poster_url and poster_url != "N/A":
                return poster_url

        return None


    def get_posters(self, titles: List[str]) -> List[str]:
        posters = []
        for title in titles:
            path = self._images_path(title)
            if path:  # If image isn`t exist
                posters.append(path)
            else:
                posters.append('assets/none.jpeg')  # Add plug

        return posters
