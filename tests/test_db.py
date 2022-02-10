from pyground import db
from pyground.db.mongo.models.items import ItemVar

import time
from datetime import datetime

db.connect(mongo={"db": "test"})

ITEMS = [
    {"name": "first"},
    {"name": "second"},
    {"name": "third"},
]


def test_create_items():
    db.Item.delete_all()
    for item in ITEMS:
        db.Item.create(**item)

    assert len(db.Item.list()) == len(ITEMS)


def test_vars():
    db.Item.delete_all()
    first = db.Item.create(name="first")
    first.set_var("color", "red")
    first.set_var("color", "green")
    assert ItemVar.objects.count() == 2
    assert first.get_var("color") == "green"


def test_vars_ts():
    db.Item.delete_all()
    first = db.Item.create(name="first")
    ts = datetime.utcnow()
    time.sleep(0.1)
    first.set_var("number", "zero", ts=ts)
    time.sleep(0.1)
    first.set_var("number", "one", ts=ts)

    first.set_var("number", "two")
    first.set_var("number", "three")
    time.sleep(0.1)
    ts = datetime.utcnow()
    time.sleep(0.1)
    first.set_var("number", "four")
    first.set_var("number", "five")
    first.set_var("number", "six")
    assert ItemVar.objects.count() == 6
    assert first.get_var_before("number", ts) == "three"
    assert first.get_var_after("number", ts) == "four"
    assert first.get_var("number") == "six"


def test_count():
    db.Item.delete_all()
    db.Item.create(name="first").set_var("color", "red")
    db.Item.create(name="second").set_var("color", "red")
    db.Item.create(name="third").set_var("color", "yellow")
    db.Item.create(name="four")

    assert db.Item.count() == 4
    assert db.Item.count(vars={"color": "red"}) == 2
