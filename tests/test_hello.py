from app.hello import hello


def test_hello_default():
    assert hello() == "Hello world!"


def test_hello_arg():
    assert hello("Jon Snow") == "Hello Jon Snow!"
