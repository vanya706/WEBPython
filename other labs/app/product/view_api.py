from functools import wraps

from flask import jsonify, request

from . import api_category_blueprint
from .models import Categoryfirm
from .. import db


def protected(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if auth and auth.username == "Ivan Mostovyi" and auth.password == "password":
            return f(*args, **kwargs)
        return jsonify({'message': 'Authentication failed!'}), 403

    return decorated


@api_category_blueprint.route('/', methods=['GET'])
def category_all():
    categories = Categoryfirm.query.all()
    return_values = []
    for category in categories:
        category_dict = {}
        category_dict['id'] = category.id
        category_dict['firm'] = category.firm
        return_values.append(category_dict)
    return jsonify({'categories': return_values})


@api_category_blueprint.route('', methods=['POST'])
@protected
def create():
    new_category = request.get_json()
    category = Categoryfirm(firm=new_category['firm'])

    db.session.add(category)
    db.session.commit()

    return jsonify({'category': {'id': category.id, 'firm': category.firm}})


@api_category_blueprint.route('/<id>', methods=['GET'])
def category(id):
    category = Categoryfirm.query.get_or_404(id)
    return jsonify({'category': {'id': category.id, 'firm': category.firm}})


@api_category_blueprint.route('/<id>', methods=['PUT'])
@protected
def update(id):
    category = Categoryfirm.query.get_or_404(id)

    updated_category = request.get_json()

    category.firm = updated_category['firm']

    db.session.add(category)
    db.session.commit()

    return jsonify({'category': {'id': category.id, 'firm': category.firm}})


@api_category_blueprint.route('/<id>', methods=['DELETE'])
@protected
def delete(id):
    category = Categoryfirm.query.get_or_404(id)
    db.session.delete(category)
    db.session.commit()
    return jsonify({'message': f'The category with id {category.id} has been deleted!'})
