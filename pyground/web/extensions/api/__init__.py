from flask_smorest import Api


def create_app(server, url_prefix):
    app = Api(server, spec_kwargs={
        "title": "PyGround API",
        "version": "v1",
        "openapi_version": "3.0.3",
    })
    register_blueprints(app, url_prefix)
    return app


def register_blueprints(app, url_prefix):
    from .blueprints import foo
    from .blueprints import bar

    app.register_blueprint(foo.bp, url_prefix=url_prefix+"/foo")
    app.register_blueprint(bar.bp, url_prefix=url_prefix+"/bar")
