from abc import ABCMeta, abstractmethod


class Beverage:
    __metaclass__ = ABCMeta

    def __init__(self):
        self.move = None

    @abstractmethod
    def setMove(self, move):
        raise NotImplementedError

    @abstractmethod
    def getMove(self):
        raise NotImplementedError
