from flask import Blueprint
from flask_login import login_required

bp = Blueprint('bar', __name__)


@bp.route('/')
@login_required
def home():
    return "Hello from Bar Blueprint"
