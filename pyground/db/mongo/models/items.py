from datetime import datetime
from functools import cache

import mongoengine as me

from . import BaseDocument


class Item(BaseDocument):
    name = me.StringField(required=True, unique=True)

    def set_var(self, var_name, var_value, ts=None):
        ItemVar(item=self, name=var_name, value=var_value, ts=ts).save()
        return self

    @cache
    def get_var(self, var_name):
        first = ItemVar.objects(item=self, name=var_name).order_by('-ts').first()
        if first is not None:
            return first.value
        else:
            return None

    def get_var_before(self, var_name, ts):
        return ItemVar.objects(item=self, name=var_name, ts__lte=ts).order_by('-ts').first().value

    def get_var_after(self, var_name, ts):
        return ItemVar.objects(item=self, name=var_name, ts__gte=ts).order_by('ts').first().value

    @classmethod
    def list(cls, vars=None, **kwargs):
        if vars is None:
            return super().list(**kwargs)
        else:
            return [item for item in super().list(**kwargs)
                    if all([item.get_var(var) == value for var, value in vars.items()])]

    @classmethod
    def count(cls, vars=None, **kwargs):
        if vars is None:
            return super().count(**kwargs)
        else:
            return len(cls.list(vars, **kwargs))


class ItemVar(me.Document):
    item = me.ReferenceField(Item, required=True, reverse_delete_rule=me.CASCADE)
    name = me.StringField(required=True)
    value = me.StringField(required=True)
    ts = me.DateTimeField(default=datetime.utcnow)
    hash = me.StringField(primary_key=True)

    def save(self, **kwargs):
        if self.hash is None:
            self.hash = f"{self.item.name}/{self.name}/{self.ts}"
        super().save(**kwargs)
