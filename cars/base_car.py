from abc import ABC, abstractmethod

class Car(ABC):
    """Abstract interface for some car"""
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def brakes(self):
        pass

    @abstractmethod
    def speed(self):
        pass
