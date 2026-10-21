from flask import Flask, render_template, jsonify, request
import requests
from tmdb import get_popular_movies, search_movies

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/movies/popular")
def popular_movies():
    try:
        movies = get_popular_movies()
        return jsonify(movies)
    except requests.RequestException:
        return jsonify({"error": "Movie service unavailable"}), 502


@app.route("/api/movies/search")
def movie_search():
    query = request.args.get("q", "").strip()

    if not query or len(query) > 100:
        return jsonify({"error": "Enter a valid movie title"}), 400

    try:
        movies = search_movies(query)
        return jsonify(movies)
    except requests.RequestException:
        return jsonify({"error": "Movie service unavailable"}), 502
