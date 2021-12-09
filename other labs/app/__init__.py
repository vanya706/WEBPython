from config import config
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy

convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}


def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config.get(config_name))
    global db
    metadata = MetaData(naming_convention=convention)
    db = SQLAlchemy(metadata=metadata)

    global login_manager
    login_manager = LoginManager(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message_category = 'warning'
    global bcrypt
    bcrypt = Bcrypt(app)

    db.init_app(app)
    migrate = Migrate(app, db, render_as_batch=True)
    migrate.init_app(app, db, render_as_batch=True)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    with app.app_context():
        from . import view

        from .auth import auth_blueprint
        app.register_blueprint(auth_blueprint, url_prefix='/auth')

        from .form_cabinet import cabinet_blueprint
        app.register_blueprint(cabinet_blueprint, url_prefix='/regcabinet')

        from .posts import post_blueprint
        app.register_blueprint(post_blueprint, url_prefix='/post')

        from .product import product_blueprint
        app.register_blueprint(product_blueprint, url_prefix='/product')

        return app
