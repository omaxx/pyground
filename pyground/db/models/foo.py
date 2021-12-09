import mongoengine as me

from .base import BaseDocument


class Foo(BaseDocument):
    name = me.StringField(required=True, unique=True)
