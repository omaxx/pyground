import marshmallow as ma


class Foo(ma.Schema):
    name = ma.fields.String(required=True)


class Bar(ma.Schema):
    name = ma.fields.String(required=True)
