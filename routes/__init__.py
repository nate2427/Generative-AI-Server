from flask import Blueprint

routes = Blueprint("routes", __name__)


def init_routes():
    from . import culture_trip_ai


init_routes()
