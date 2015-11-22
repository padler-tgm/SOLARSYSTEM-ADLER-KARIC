from abc import ABCMeta, abstractmethod
from panda3d.core import Vec3, Vec4


class Move:
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def update(self, planet):
        raise NotImplementedError