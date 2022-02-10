import mongoengine as me

from . import models
from . import errors


def connect(host=None, db=None, username=None, password=None):
    me.connect(
        host=host,
        db=db or __name__.split(".")[0],
        username=username,
        password=password,
        authentication_source='admin',
    )


def disconnect():
    me.disconnect()