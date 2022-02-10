import mongoengine as me

from .. import errors


class BaseDocument(me.Document):
    meta = {
        'abstract': True,
    }

    @classmethod
    def get(cls, **kwargs):
        try:
            return cls.objects.get(**kwargs)
        except me.DoesNotExist:
            raise errors.DoesNotExist()

    @classmethod
    def create(cls, **kwargs):
        try:
            return cls(**kwargs).save()
        except me.NotUniqueError:
            raise errors.AlreadyExist()

    @classmethod
    def list(cls, **kwargs):
        return cls.objects(**kwargs)

    @classmethod
    def count(cls, **kwargs):
        return cls.objects.count(**kwargs)

    @classmethod
    def delete_all(cls):
        # cls.drop_collection()
        cls.objects.delete()


from .bar import Bar
from .foo import Foo
from .users import User
from .items import Item
