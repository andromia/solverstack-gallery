import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
import os
from flask import Flask, request, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_caching import Cache
from config import Config
__version__ = 'v0.0.0'


# TODO: register 'static' folder to app
ROOT = Config.ROOT

db = SQLAlchemy()
migrate = Migrate()
bootstrap = Bootstrap()
cache = Cache()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    bootstrap.init_app(app)
    cache.init_app(app)

    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app
