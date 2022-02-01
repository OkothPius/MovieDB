import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    '''
    General configuration parent class
    '''
    MOVIE_API_BASE_URL= 'https://api.themoviedb.org/3/movie/{}?api_key={}'
    MOVIE_API_KEY = os.getenv('MOVIE_API_KEY')
    SECRET_KEY = os.getenv('SECRET_KEY')


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
