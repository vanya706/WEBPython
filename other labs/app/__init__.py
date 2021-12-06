from config import config
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config.get(config_name))
    global db
    db = SQLAlchemy(app)
    migrate = Migrate(app, db)

    global login_manager
    login_manager = LoginManager(app)
    login_manager.login_view = 'login'
    login_manager.login_message_category = 'warning'
    global bcrypt
    bcrypt = Bcrypt(app)

    migrate = Migrate(app, db)
    db.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    with app.app_context():
        from . import view

        from .auth import auth_blueprint
        app.register_blueprint(auth_blueprint, url_prefix='/auth')

        from .form_cabinet import cabinet_blueprint
        app.register_blueprint(cabinet_blueprint, url_prefix='/regcabinet')

        return app
