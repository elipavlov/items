# coding=utf-8
from sqlite3 import IntegrityError

from flask import json, request, url_for, flash, jsonify, session
from items.exceptions import DataExtractionError
from sqlalchemy import exc

from .config import app
from .models import db, Item

from logging import getLogger

logger = getLogger(__name__)


def _process_error_response(error):
    flash(str(error))

    return app.response_class(
        response=json.dumps(dict(
            status='fail',
            error_type=type(error).__name__,
            error=str(error))),
        status=400,
        mimetype='application/json'
    )


@app.route('%sadd' % app.config.get('API_PATH'), methods=['POST'])
def add_item():
    data = None
    try:
        data = json.loads(request.data)
    except ValueError as e:
        flash('Data decoding error')
        response = _process_error_response(e)

    if data:
        try:
            item = Item(**data)

            db.session.add(item)
            db.session.commit()
            response = jsonify(status='ok')
        except (IntegrityError, exc.IntegrityError) as e:
            print(str(e))
            logger.warning(str(e))

            db.session.rollback()
            response = _process_error_response(
                ValueError('Unpropper input data')
            )

        except (TypeError, DataExtractionError) as e:
            response = _process_error_response(e)

    return response


@app.route('%sitems' % app.config.get('API_PATH'))
def get_items_list():
    flash('New items was successfully added')
    items = [row.serialize() for row in db.session.query(Item).all()]
    response = jsonify(status='ok', items=items)
    return response


@app.route('%sitems/' % app.config.get('API_PATH'), defaults={'path': ''})
@app.route('%sitems/<path:path>' % app.config.get('API_PATH'))
def get_item(path):
    flash('New items was successfully added')
    # response = jsonify(status='ok')
    response = app.response_class(
        response=json.dumps(dict(status='ok')),
        status=200,
        mimetype='application/json'
    )
    return response
