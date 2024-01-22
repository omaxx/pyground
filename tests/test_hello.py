from app.hello import hello


def test_hello_default() -> None:
    assert hello() == "Hello, World!"


def test_hello_arg() -> None:
    assert hello(name="Jon Snow") == "Hello, Jon Snow!"
