from flask import Blueprint

product_blueprint = Blueprint('product', __name__, template_folder="templates")
api_category_blueprint = Blueprint('api_category', __name__)

from . import view
from . import view_api