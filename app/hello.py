import logging

logger = logging.getLogger(__name__)


def hello(greet: str = "Hello", name: str = "World") -> str:
    logger.info(f"{name}: use greet `{greet}`")
    return f"{greet}, {name}!"
