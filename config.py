import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MOVIE_API_BASE_URL= 'https://api.themoviedb.org/3/movie/{}?api_key={}'
    MOVIE_API_KEY = os.getenv('MOVIE_API_KEY')
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://watchlist:pyglass@localhost/watchlist'


class ProdConfig(Config):

    pass


class DevConfig(Config):

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
