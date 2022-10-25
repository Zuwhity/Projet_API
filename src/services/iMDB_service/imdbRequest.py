import requests
import os
from dotenv import load_dotenv
from .response import Response

class ImdbRequest:
    _imdb_url = "https://imdb-api.com/en/API"
    load_dotenv()
    api_key=os.getenv('IMDB_API_KEY')

    @classmethod
    def get_movies(cls, expression):
        response = requests.get(cls._imdb_url+'/SearchMovie/'+cls.api_key+'/'+expression)
        return Response(status_code=response.status_code, content=response.json())

    
    @classmethod
    def get_ratings(cls, id_movie):
        response = requests.get(cls._imdb_url+'/Ratings/'+cls.api_key+'/'+id_movie)
        return Response(status_code=response.status_code, content=response.json())

    @classmethod
    def get_reviews(cls, id_movie):
        response = requests.get(cls._imdb_url+'/Reviews/'+cls.api_key+'/'+id_movie)
        return Response(status_code=response.status_code, content=response.json())
