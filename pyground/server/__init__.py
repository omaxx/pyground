from flask import Flask


def create_app():
    from .config import BaseConfig

    app = Flask(__name__)
    app.config.from_object(BaseConfig)

    from . import routes

    register_blueprints(app)
    register_extensions(app)

    return app


def register_blueprints(app):
    from .blueprints import foo
    from .blueprints import bar

    app.register_blueprint(foo.bp, url_prefix='/foo')
    app.register_blueprint(bar.bp, url_prefix='/bar')


def register_extensions(app):
    from .extensions import api
    from .extensions import dash

    api.create_app(app, url_prefix='/api')
    dash.create_app(app, url_prefix='/dash')
