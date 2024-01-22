from app.hello import hello


def test_hello_default() -> None:
    assert hello() == "Hello world!"


def test_hello_arg() -> None:
    assert hello("Jon Snow") == "Hello Jon Snow!"
