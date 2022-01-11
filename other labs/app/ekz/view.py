from flask import request, jsonify, current_app
from flask_restful import Resource, Api, fields, marshal_with

from .. import db
from ..product.models import Product

product_template = {
    'id': fields.Integer,
    'name': fields.String,
    'price': fields.String,
    'type': fields.String,
    'number': fields.String,
    'date': fields.String,
    'category_firm': fields.Integer,
    'user_id': fields.Integer
}


class ProductHandlerApi(Resource):
    @marshal_with(product_template)
    def get(self, id):
        return Product.query.get_or_404(id)

    @marshal_with(product_template)
    def post(self, id):
        data = request.get_json()
        product_new = Product(
            id=data['id'],
            name=data['name'],
            price=data['price'],
            type=data['type'],
            number=data['number'],
            date=data['date'],
            category_firm=data['category_firm'],
            user_id=data['user_id']
        )

        db.session.add(product_new)
        db.session.commit()
        return product_new

    @marshal_with(product_template)
    def put(self, id):
        data = request.get_json()
        product_old = Product.query.get_or_404(id)
        product_new = Product(
            id=data['id'],
            name=data['name'],
            price=data['price'],
            type=data['type'],
            number=data['number'],
            date=data['date'],
            category_firm=data['category_firm'],
            user_id=data['user_id']
        )

        product_old.id = product_new.id
        product_old.name = product_new.name
        product_old.price = product_new.price
        product_old.type = product_new.type
        product_old.number = product_new.number
        product_old.date = product_new.date
        product_old.category_firm = product_new.category_firm
        product_old.user_id = product_new.user_id

        db.session.commit()
        return product_old

    def delete(self, id):
        product = Product.query.get(id)
        db.session.delete(product)
        db.session.commit()
        return jsonify({'message': 'The product has been deleted!'})


class ProductsHandlerApi(Resource):
    @marshal_with(product_template)
    def get(self):
        print(Product.query.all())
        return Product.query.all()


api = Api(current_app)
api.add_resource(ProductHandlerApi, "/api/mostovyi/product/<int:id>")
api.add_resource(ProductsHandlerApi, "/api/mostovyi/products")
