from flask import Blueprint

bp = Blueprint('bar', __name__)


@bp.route('/')
def home():
    return "Hello from Bar Blueprint"
