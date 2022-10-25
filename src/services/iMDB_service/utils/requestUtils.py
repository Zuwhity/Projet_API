from src.services.iMDB_service import response


from ..imdbRequest import ImdbRequest

def get_first_result(response_content):
    return response_content['results'][0]

def get_movie_id(movie):
    return movie['id']

def get_movie_reviews(movie):
    movie_id = get_movie_id(movie)
    reviews_reponse = ImdbRequest.get_reviews(movie_id)
    return reviews_reponse


def get_movie_ratings(movie):
    movie_id = get_movie_id(movie)
    ratings_response = ImdbRequest.get_ratings(movie_id)
    return ratings_response

