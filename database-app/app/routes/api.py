from flask import Blueprint, jsonify
import datetime

bp = Blueprint('api', __name__, url_prefix='/api')


@bp.route('/')
def index():
    return jsonify({
        'data': 'hello world'
    })


@bp.route('/utils/clock')
def clock():
    return jsonify({
        'data': datetime.datetime.now().isoformat()
    })
