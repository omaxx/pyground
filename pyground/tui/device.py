from dataclasses import dataclass
import time
import random

from .observer import Observable


@dataclass
class Device(Observable):
    name: str
    ip: str
    username: str
    password: str
    status: str = ""
    version: str = ""

    def __post_init__(self):
        Observable.__init__(self)

    def update(self):
        time.sleep(random.randint(0, 5))
        self.status = "CONNECTED"
        self.notify_observers()
        time.sleep(random.randint(0, 5))
        self.version = f"v{random.randint(0, 5)}"
        self.notify_observers()

