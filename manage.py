from app import create_app

from flask_script import Manager, Server
from . import tests

app = create_app('development')

manager = Manager(app)
manager.add_command('server',Server)

@manager.command
tests


if __name__ == '__main__':
	"""this code executes if this file is run as the main file"""
	manager.run()