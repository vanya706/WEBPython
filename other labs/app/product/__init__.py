from flask import Blueprint

product_blueprint = Blueprint('product', __name__, template_folder="templates")

from . import view