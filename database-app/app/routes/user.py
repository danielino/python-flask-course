from flask import Blueprint, jsonify, request
from app.models.user import User
from app.models.base import db

bp = Blueprint('user', __name__, url_prefix='/user')


@bp.route('/')
def index():
    return jsonify({
        'data': [x.serialize() for x in User.query.all()]
    })


@bp.route("/", methods=["POST"])
def create():
    try:
        data = request.form
        username = data['username']
        email = data['email']

        u = User(username=username, email=email)
        db.session.add(u)
        db.session.commit()
        return jsonify({
            "id": u.id
        })
    except Exception as e:
        return jsonify({
            "operation": "create",
            "status": "error",
            "error": str(e)
        })


@bp.route("/<int:id>", methods=["GET"])
def search(id):
    u = User.query.filter_by(id=id).first()
    if u:
        return jsonify(u.serialize())
    return jsonify({
        "operation": "search",
        "status": "error",
        "error": "user not found"
    }), 205


@bp.route("/<int:id>", methods=["DELETE"])
def delete(id):
    u = User.query.filter_by(id=id).first()
    if u:
        db.session.delete(u)
        db.session.commit()
        return jsonify({"operation": "delete", "status": "ok"})
    return jsonify({"operation": "delete", "status": "error"}), 205
