from flask import request

from functools import wraps

import settings

class Handler():
    def __init__(self):
        self.services = {}  # format is {path: callable}

    def register(self, app):
        for path, func in self.services.iteritems():
            if func.__code__.co_argcount == 1:
                app.route(path, methods=["POST"])(check_header(func))

    @staticmethod
    def package_response(response):
        return str(response)


def check_header(func):
    @wraps(func)
    def func_wrapper():
        api_key = request.headers.get("x-api-key", None)
        if api_key is None:
            raise ValueError("API Key not found")
        if api_key != settings.API_KEY:
            raise ValueError("API Key invalid")
        return func()
    return func_wrapper
