from app import create_app, db
from app.models import User
# from flask.cli
# import FlaskGroup

from flask_script import Manager, Server

# Creating an app instance
app = create_app('development')

manager = Manager(app)
# cli = FlaskGroup(app)

manager.add_command('server', Server)

@manager.command
def test():
    """ Run the unit test. """
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User)

if __name__ == '__main__':
    manager.run()
