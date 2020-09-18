from flask_sqlalchemy import SQLAlchemy
import os
from sqlalchemy.inspection import inspect


db = SQLAlchemy()


class ModelSerializer():

    def serialize(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}
