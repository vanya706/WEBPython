from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisisasecret!'
app.config['WTF_CRSF_ENAVLED'] = True

# do not remove
from app import view