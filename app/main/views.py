from flask import render_template, redirect, url_for
from flask_login import login_required
from . import main
from ..request import get_movies, get_movie
from ..models import Review
from .forms import ReviewForm


# Views
@main.route('/')
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

@main.route('/movie/<int:id>')
def movie(id: int):
    '''
    View movie page function that returns the movie details page and its data
    '''
    movie = get_movie(id)
    title = f'{movie.title}'
    reviews = Review.get_reviews(movie.id)

    return render_template('movie.html', movie=movie, title=title, reviews=reviews)


@main.route('/movie/review/new/<int:id>', methods=['GET','POST'])
@login_required
def new_review(id):
    form = ReviewForm()
    movie = get_movie(id)

    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data
        new_review = Review(movie.id, title, movie.poster, review)
        new_review.save_review()
        return redirect(url_for('main.movie', id = movie.id))

    title = f'{movie.title} review'
    return render_template('new_review.html', title=title, review_form=form, movie=movie)
