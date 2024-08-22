from datetime import timedelta
from flask import Flask
from flask.blueprints import Blueprint
from flask_cors import CORS

from flask.cli import with_appcontext

from utils import handle_exception, response

import config as config
import routes as routes


"""Create an application."""
server = Flask(__name__)

"""Server Configuration"""
server.debug = config.DEBUG

"""CORS Configuration"""
CORS(server)


@server.route("/")
def main():
    return response(
        200,
        True,
        "Api Is Working",
    )


@server.errorhandler(Exception)
def handle_error(e):
    return handle_exception(e)


for blueprint in vars(routes).values():
    if isinstance(blueprint, Blueprint):
        server.register_blueprint(
            blueprint, url_prefix=config.APPLICATION_ROOT)

if __name__ == "__main__":
    server.run(host=config.HOST, port=int(config.PORT))
