from flask import Blueprint

bp = Blueprint('test', __name__, url_prefix='/test')


@bp.route('/')
def index():
    return "bp_test_index"
