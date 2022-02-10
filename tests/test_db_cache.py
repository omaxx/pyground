from pyground import db


def test_vars_cache():
    db.connect(mongo={"db": "test"})
    db.Item.delete_all()
    first = db.Item.create(name="first")
    second = db.Item.create(name="second")
    first.set_var("color", "red")
    second.set_var("color", "yellow")
    assert first.get_var("color") == "red"
    assert second.get_var("color") == "yellow"
    db.disconnect()
    assert first.get_var("color") == "red"
    assert second.get_var("color") == "yellow"
