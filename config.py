import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
	
	DEBUG = False
	DEVELOPMENT = False
	
	SECRET_KEY = os.environ.get("SECRET_KEY", os.urandom(24))
	
	SQLALCHEMY_ECHO = False
	SQLALCHEMY_TRACK_MODIFICATIONS = False

	@staticmethod
	def init_app(app):
		pass


class DevConfig(Config):
	DEBUG = True
	DEVELOPMENT = True
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
		"sqlite:///" + os.path.join(BASE_DIR, 'dev.sqlite3')


class ProdConfig(Config):
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
		"sqlite:///" + os.path.join(BASE_DIR, 'prod.sqlite3')

	@classmethod
	def init_app(cls, app):
		Config.init_app(app)


config = {
    "prod": ProdConfig,
    "dev": DevConfig,
}
