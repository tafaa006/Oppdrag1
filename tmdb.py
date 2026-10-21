
import os
import requests
from dotenv import load_dotenv

load_dotenv()

TMDB_API_KEY = os.getenv("TMDB_API_KEY")
TMDB_BASE_URL = "https://api.themoviedb.org/3"


def get_popular_movies():
    if not TMDB_API_KEY:
        raise RuntimeError("TMDB_API_KEY is not configured")

    response = requests.get(
        f"{TMDB_BASE_URL}/movie/popular",
        params={
            "api_key": TMDB_API_KEY,
            "language": "en-US",
            "page": 1
        },
        timeout=10
    )

    response.raise_for_status()
    return response.json()["results"]


def search_movies(query):
    if not TMDB_API_KEY:
        raise RuntimeError("TMDB_API_KEY is not configured")

    response = requests.get(
        f"{TMDB_BASE_URL}/search/movie",
        params={
            "api_key": TMDB_API_KEY,
            "query": query,
            "language": "en-US"
        },
        timeout=10
    )

    response.raise_for_status()
    return response.json()["results"]
