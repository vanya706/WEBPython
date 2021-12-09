import enum

from .. import db


class Categoryfirm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firm = db.Column(db.String(50), nullable=False)
    product = db.relationship('Product', backref='category', lazy=True)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    price = db.Column(db.String(60), nullable=False)
    type = db.Column(db.String(60), nullable=False)
    number = db.Column(db.String(60), nullable=False)
    date = db.Column(db.String(60), nullable=False) 
    category_firm = db.Column(db.Integer, db.ForeignKey('categoryfirm.id'), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)



    def __repr__(self):
        return f"Post('{self.id}', '{self.name}')"