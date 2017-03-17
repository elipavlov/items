# coding=utf-8

from datetime import datetime, timedelta

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

    def exired(self):
        return (datetime.now() - self.start_time) > timedelta(days=self.days, seconds=3600*12)

    def serialize(self):
        tdl = (datetime.now() - self.start_time)
        if tdl.days >= self.days:
            perc = self.end_percent
            price = self.start_price*self.end_percent*0.01
            is_min = True
        else:
            is_min = False
            perc = (100 - ((100-self.end_percent)/self.days)*tdl.days)
            price = self.start_price \
                * perc\
                * 0.01

        res = dict(
            id=self.id,
            is_price_min=is_min,
            current_price=price,
            # start_price=self.start_price,
            # percent=perc,
            # days=tdl.days,
            # start=self.start_time,
        )
        return res

    def __init__(self, **kwargs):
        self.extract(**kwargs)

    def __repr__(self):
        return '<Item (id=%s, start_time=%s>' % (self.id, self.start_time)
