from abc import ABCMeta, abstractmethod


class Move:
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def update(self, planet):
        raise NotImplementedError