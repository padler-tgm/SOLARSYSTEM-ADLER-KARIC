from abc import ABCMeta, abstractmethod
from Beverage import Beverage

class CondimentDecorator(Beverage):
    __metaclass__ = ABCMeta

    def setMove(self, move):
        self.move = move