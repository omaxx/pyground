from . import mongo as mongodb
from .mongo.models import *


def connect(mongo=None):
    mongodb.connect(**(mongo or {}))


def disconnect():
    mongodb.disconnect()
