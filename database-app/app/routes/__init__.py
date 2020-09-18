from .test import bp as bp_test
from .api import bp as bp_api
from .user import bp as bp_user


def init_app(app):
    app.register_blueprint(bp_test)
    app.register_blueprint(bp_api)
    app.register_blueprint(bp_user)
