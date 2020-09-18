from app import create_app
from app.models.base import db
import os


app = create_app()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()


def main():
    return app


if __name__ == "__main__":
    app.run(debug=True)
