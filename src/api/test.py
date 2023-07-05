import os
from dotenv import load_dotenv
from omdb import OMDBApi

load_dotenv()
api_key = os.getenv("API_KEY")

if __name__ == "__main__":
    api = OMDBApi(api_key)
    posters = api.get_posters(['The Dark Knight', 'Pirates of the Caribbean'])
    print(posters)
