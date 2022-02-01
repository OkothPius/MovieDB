from app import create_app
# from flask.cli
# import FlaskGroup

from flask_script import Manager, Server

# Creating an app instance
app = create_app('development')

manager = Manager(app)
# cli = FlaskGroup(app)

manager.add_command('server', Server)

if __name__ == '__main__':
    manager.run()
