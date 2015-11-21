from abc import ABCMeta, abstractmethod
from subjects.Planet import *


class Move:
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def update(self, planet):
        raise NotImplementedError