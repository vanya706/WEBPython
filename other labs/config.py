import os

basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = 'This is my very secret key, which i will put to env variables'
WTF_CRSF_ENAVLED = True
# Database
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                          'sqlite:///' + os.path.join(basedir, 'form.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
