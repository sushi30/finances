import os
from flask import Flask
from flask_compress import Compress
from flask_cors import CORS
from flask_login import LoginManager
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from app.assets import app_css, app_js, vendor_css, vendor_js
from config import config as Config

basedir = os.path.abspath(os.path.dirname(__file__))

mail = Mail()
db = SQLAlchemy()
csrf = CSRFProtect()
compress = Compress()


# Set up Flask-Login
login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "account.login"


def create_app(config):
    app = Flask(__name__)
    config_name = config

    if not isinstance(config, str):
        config_name = os.getenv("FLASK_CONFIG", "default")

    app.config.from_object(Config[config_name])
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    # not using sqlalchemy event system, hence disabling it

    Config[config_name].init_app(app)

    db.init_app(app)
    login_manager.init_app(app)
    CORS(app)

    # Configure SSL if platform supports it
    if not app.debug and not app.testing and not app.config["SSL_DISABLE"]:
        from flask_sslify import SSLify

        SSLify(app)

    # fmt: off
    # Create app blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .api import blueprint as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix="/api")

    # fmt: on

    return app
