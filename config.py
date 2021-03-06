import os
import re
from dotenv import load_dotenv

load_dotenv()

class Config:
    MOVIE_API_BASE_URL= 'https://api.themoviedb.org/3/movie/{}?api_key={}'
    MOVIE_API_KEY = os.getenv('MOVIE_API_KEY')
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)
# rest of connection code using the connection string `uri`



class ProdConfig(Config):

    pass

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://watchlist:pyglass@localhost/watchlist_test'

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://watchlist:pyglass@localhost/watchlist'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}
