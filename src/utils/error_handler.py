from werkzeug.exceptions import HTTPException
from flask import current_app
from utils import response


def handle_exception(e):
    if isinstance(e, HTTPException):
        return response({"message": e.description}, e.code)

    return response(500, False, {"message": str(e)})
