import mongoengine as me

from . import BaseDocument


class Bar(BaseDocument):
    name = me.StringField(required=True, unique=True)
