import os

basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = 'This is my very secret key, which i will put to env variables'
WTF_CRSF_ENAVLED = True

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'site.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
