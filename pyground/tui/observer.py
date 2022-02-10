from abc import ABC
from typing import Protocol


class Observer(Protocol):
    def update(self):
        pass


class Observable(ABC):
    def __init__(self) -> None:
        self.observers = []

    def register_observer(self, observer: Observer) -> None:
        self.observers.append(observer)

    def notify_observers(self) -> None:
        for observer in self.observers:
            observer.update()
