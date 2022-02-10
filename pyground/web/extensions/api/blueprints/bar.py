from http import HTTPStatus

from flask.views import MethodView
from flask_smorest import Blueprint

from pyground import db
from .. import schema

bp = Blueprint("bar-api", __name__)


@bp.route("")
class BarList(MethodView):
    @bp.response(HTTPStatus.OK, schema.Bar(many=True))
    def get(self):
        """Get Bar list"""
        return db.Bar.list()

    @bp.arguments(schema.Bar, as_kwargs=True)
    @bp.response(HTTPStatus.CREATED)
    def post(self, **kwargs):
        return db.Bar.create(**kwargs)


@bp.route("/<uid>")
class Bar(MethodView):
    @bp.response(HTTPStatus.OK, schema.Bar)
    def get(self, uid):
        """Get Bar info"""
        return db.Bar.get(name=uid)
