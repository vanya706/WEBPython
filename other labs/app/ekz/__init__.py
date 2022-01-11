from flask import Blueprint

api_ekz_blueprint = Blueprint('api_ekz', __name__)

from . import view