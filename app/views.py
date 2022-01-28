from flask import render_template
from app import app

# Views
@app.route('/')
def index():
    '''
    view root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('index.html', title=title)

@app.route('/movies/<int:movie_id>')
def movie(movie_id: int):
    return render_template('movie.html', id=movie_id)
