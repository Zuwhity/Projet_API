# import sys
# sys.path.insert(0, sys.path+'/')
import os


import os

from src.services.iMDB_service.utils.requestUtils import *
from src.services.iMDB_service.imdbRequest import ImdbRequest
#print(ImdbRequest.get_movies('leon the professional').content)
#print(ImdbRequest.get_ratings('tt1375666').content)
# movies = ImdbRequest.get_movies('leon the professional').content
# print(get_id_from_movie(get_first_result(movies)))

movies = ImdbRequest.get_movies('inception').content
best_movie_result = get_first_result(movies)
print(get_movie_ratings(best_movie_result).content)
print(get_movie_reviews(best_movie_result).content)

