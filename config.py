from os import path
DEBUG = True

basedir = path.abspath(path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + path.join(basedir,'database.sqlite')
SQLALCHEMY_TRACK_MODIFICATIONS = True


SECRET_KEY = 'asdfghfgf!'

