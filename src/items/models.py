# coding=utf-8

from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from .exceptions import DataExtractionError

db = SQLAlchemy()


def install_db(app):
    db.init_app(app)
    return app


def init_db():
    db.create_all()


def drop_db():
    db.drop_all()


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime, default=datetime.utcnow)
    days = db.Column(db.Integer, server_default=db.text('0'))
    end_percent = db.Column(db.Integer, server_default=db.text('100'))
    start_price = db.Column(db.Float(precision=2), nullable=False)

    def extract(self, **data):
        for key in data.keys():
            if hasattr(self, key):
                if key == 'start_time':
                    try:
                        val = datetime.strptime(data[key], '%Y-%m-%d %H:%M:%S.%f')
                    except ValueError:
                        raise DataExtractionError('Wrong datetime format')

                    setattr(self, key, val)
                else:
                    setattr(self, key, data[key])

    def serialize(self):
        res = dict(
            id=self.id,
            current_price=self.start_price,
            is_price_min=False
        )
        return res

    def __init__(self, **kwargs):
        self.extract(**kwargs)

    def __repr__(self):
        return '<Item (id=%s, start_time=%s>' % (self.id, self.start_time)
