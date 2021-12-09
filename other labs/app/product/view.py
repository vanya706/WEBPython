from ..auth.models import Posts
import os
import secrets

from flask import url_for, render_template, flash, redirect, current_app
from flask_login import current_user, login_required,login_user, logout_user

from . import product_blueprint
from .forms import AddProductForm, CategoryForm
from .models import Categoryfirm, Product
from .. import db


@product_blueprint.route('/', methods=['GET', 'POST'])
@login_required
def view_prod():
    product = Product.query.order_by(Product.name).all()
    return render_template('view_product.html', product=product)


@product_blueprint.route('/addprod', methods=['GET', 'POST'])
@login_required
def add_prod():
    form = AddProductForm()
    form.category.choices = [(category.id, category.firm) for category in Categoryfirm.query.all()]
    if form.validate_on_submit():
        product = Product(name=form.name.data, price=form.price.data, type=form.type.data, number=form.number.data,
                          date=form.date.data, category_firm=form.category.data, user_id=current_user.id)
        
        db.session.add(product)
        db.session.commit() 
        flash('Your product has been add!', category='success')
        return redirect(url_for('product.view_prod'))
    
    return render_template('product_create.html', form=form)


@product_blueprint.route('/<id>', methods=['GET', 'POST'])
def detail_prod(id):
    product = Product.query.get_or_404(id)
    return render_template('product_detail.html', pk=product)


@product_blueprint.route('/delete/<id>', methods=['GET', 'POST'])
def delete_prod(id):
    product = Product.query.get_or_404(id)
    if current_user.id == product.user_id:
        db.session.delete(product)
        db.session.commit()
        return redirect(url_for('product.view_prod'))

    flash('This is not your post', category='warning')
    return redirect(url_for('product.detail_prod', pk=id))


@product_blueprint.route('/edit/<id>', methods=['GET', 'POST'])
def edit_prod(id):
    product = Product.query.get_or_404(id)
    if current_user.id != product.user_id:
        flash('This is not your post', category='warning')
        return redirect(url_for('prod.detail_prod', pk=product))

    form = AddProductForm()
    form.category.choices = [(category.id, category.firm) for category in Categoryfirm.query.all()]

    if form.validate_on_submit():
        product.name = form.name.data
        product.price = form.price.data
        product.type = form.type.data
        product.number = form.number.data
        product.date = form.date.data
        product.category_firm = form.category.data

        db.session.add(prouct)
        db.session.commit()

        flash('Product has been update', category='access')
        return redirect(url_for('prod.detail_prod', id=id))

        form.name.data = product.name
        form.price.data = product.price
        form.type.data = product.type
        form.number.data = product.numder
        form.date.data = product.date
        form.category.data = product.category_firm 
    

    return render_template('product_create.html', form=form)


@product_blueprint.route('/categoryrcrud', methods=['GET', 'POST'])
def category_crud():
    form = CategoryForm()

    if form.validate_on_submit():
        category = Categoryfirm(firm=form.name.data)

        db.session.add(category)
        db.session.commit()
        flash('Категорія добавленна')
        return redirect(url_for('.category_crud'))

    categories = Categoryfirm.query.all()
    return render_template('category_crud.html', categories=categories, form=form)


@product_blueprint.route('/update_category/<id>', methods=['GET', 'POST'])
def update_category(id):
    category = Categoryfirm.query.get_or_404(id)
    form = CategoryForm()
    if form.validate_on_submit():
        category.firm = form.name.data

        db.session.add(category)
        db.session.commit()
        flash('Категорія відредагована')
        return redirect(url_for('.category_crud'))

    form.name.data = category.firm
    categories = Categoryfirm.query.all()
    return render_template('category_crud.html', categories=categories, form=form)


@product_blueprint.route('/delete_category/<id>', methods=['GET'])
@login_required
def delete_category(id):
    category = Categoryfirm.query.get_or_404(id)
    db.session.delete(category)
    db.session.commit()

    flash('Category delete', category='access')
    return redirect(url_for('.category_crud'))        