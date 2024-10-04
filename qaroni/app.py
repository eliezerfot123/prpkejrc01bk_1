# -*- coding: utf-8 -*-
"""The app module, containing the app factory function."""
import logging
import sys

from flask import Flask, render_template
from environs import Env
from qaroni import commands
from apps.user import *
from qaroni.extensions import (
    bcrypt,
    cache,
    db,
    migrate,
    mail,
    jwt,
)

from apps.user.views import users_blueprint_api
from apps.books.views import books_blueprint_api
from flasgger import Swagger
from qaroni.swagger_template import template as swagger_template



def create_app(config_object="qaroni.settings"):
    """Create application factory, as explained here: http://flask.pocoo.org/docs/patterns/appfactories/.

    :param config_object: The configuration object to use.
    """
    app = Flask(__name__.split(".")[0])
    app.config.from_object(config_object)

    # configure mail
    env = Env()
    env.read_env()
    app.config["MAIL_SERVER"] = env.str("MAIL_SERVER")
    app.config["MAIL_PORT"] = env.int("MAIL_PORT")
    app.config["MAIL_USERNAME"] = env.str("MAIL_USERNAME")
    app.config["MAIL_PASSWORD"] = env.str("MAIL_PASSWORD")
    app.config["MAIL_USE_TLS"] = env.bool("MAIL_USE_TLS")
    app.config["MAIL_USE_SSL"] = env.bool("MAIL_USE_SSL")
    app.config['JWT_SECRET_KEY'] = env.str("JWT_SECRET_KEY") 


    register_extensions(app)
    register_blueprints(app)
    register_errorhandlers(app)
    register_shellcontext(app)
    register_commands(app)
    configure_logger(app)
    return app


def register_extensions(app):
    """Register Flask extensions."""
    cache.init_app(app)
    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)
    jwt.init_app(app)
    Swagger(app, template=swagger_template)
    return None


def register_blueprints(app):
    """Register Flask blueprints."""
    app.register_blueprint(users_blueprint_api)
    app.register_blueprint(books_blueprint_api)
    return None


def register_errorhandlers(app):
    """Register error handlers."""

    def render_error(error):
        """Render error template."""
        # If a HTTPException, pull the `code` attribute; default to 500
        error_code = getattr(error, "code", 500)
        return render_template(f"{error_code}.html"), error_code

    for errcode in [401, 404, 500]:
        app.errorhandler(errcode)(render_error)
    return None


def register_shellcontext(app):
    """Register shell context objects."""

    def shell_context():
        """Shell context objects."""
        return {"db": db, "User": user.models.User}

    app.shell_context_processor(shell_context)


def register_commands(app):
    """Register Click commands."""
    app.cli.add_command(commands.test)
    app.cli.add_command(commands.lint)


def configure_logger(app):
    """Configure loggers."""
    handler = logging.StreamHandler(sys.stdout)
    if not app.logger.handlers:
        app.logger.addHandler(handler)
