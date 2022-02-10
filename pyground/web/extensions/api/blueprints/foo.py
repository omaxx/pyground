from http import HTTPStatus

from flask.views import MethodView
from flask_smorest import Blueprint

from pyground import db
from .. import schema

bp = Blueprint("foo-api", __name__)


@bp.route("")
class FooList(MethodView):
    @bp.response(HTTPStatus.OK, schema.Foo(many=True))
    def get(self):
        """Get Foo list"""
        return db.Foo.list()

    @bp.arguments(schema.Foo, as_kwargs=True)
    @bp.response(HTTPStatus.CREATED, schema.Foo)
    def post(self, **kwargs):
        return db.Foo.create(**kwargs)


@bp.route("/<uid>")
class Foo(MethodView):
    @bp.response(HTTPStatus.OK, schema.Foo)
    def get(self, uid):
        """Get Foo info"""
        return db.Foo.get(name=uid)
