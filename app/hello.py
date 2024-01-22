import logging

logger = logging.getLogger(__name__)


def hello(greet: str = "Hello", name: str = "World") -> str:
    if name == "World":
        logger.warning(f"use default name `{name}`")
    else:
        logger.info(f"use name `{name}`")
    return f"{greet}, {name}!"
