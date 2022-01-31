from flask import render_template
from app import app
from .request import get_movies, get_movie

# Views
@app.route('/')
def index():
    '''
    view root page function that returns the index page and its data
    '''

    # Getting popular movie
    popular_movies = get_movies('popular')
    upcoming_movie = get_movies('upcoming')
    now_showing_movie = get_movies('now_playing')
    title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('index.html', title=title, popular=popular_movies,
                                            upcoming=upcoming_movie,
                                            now_playing=now_showing_movie)

@app.route('/movies/<int:id>')
def movie(id: int):
    '''
    View movie page function that returns the movie details page and its data
    '''
    movie = get_movie(id)
    title = f'{movie.title}'
    return render_template('movie.html', movie=movie, title=title)
