import unittest
from app.models import Movie


class MovieTest(unittest.Testcase):
    '''
    Test class to test the behaviour of the class
    '''

    def setUp(self):
        '''
        Set up method that will run before every test
        '''
        self.new_movie = Movie(1234, 'Python must be crazy',
                                'thrilling new series',
                                'https://image.tmdb.org/t/p/w500/khsjha27hbs',
                                8.5, 129993)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_movie, Movie))
