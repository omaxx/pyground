import mongoengine as me

from . import BaseDocument


class Foo(BaseDocument):
    name = me.StringField(required=True, unique=True)
