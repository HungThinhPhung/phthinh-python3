import logging
import traceback

from flask import jsonify
from functools import wraps

SUCCESS = 200
UNKNOWN_EXCEPTION = 1000


def format_api_result(func):
    @wraps(func)
    def execute(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return jsonify({
                'code': SUCCESS,
                'status': 'success',
                'data': result,
                'message': None,
            })
        except Exception as ex:
            logging.error(traceback.format_exc())
            code = ex.__dict__.get('code', None)
            if code is not None:
                return jsonify({
                    'code': code,
                    'status': 'error',
                    'data': None,
                    'message': str(ex)
                })
            return jsonify({
                'code': UNKNOWN_EXCEPTION,
                'status': 'error',
                'data': None,
                'message': str(ex)})
    return execute
