from abc import ABCMeta, abstractmethod
from panda3d.core import Vec3, Vec4
from direct.interval.IntervalGlobal import *

author = 'Philipp Adler'
author = 'Adin Karic'
version = '2015-11-29'
class Move:
    """
    Interface fuer die Bewegung des Planeten
    """
    __metaclass__ = ABCMeta

    def __init__(self):
        """
        Leerer Konstruktor
        """
        pass

    @abstractmethod
    def update(self, planet):
        """
        Der uebergebene Planet wird bewegt
        :param planet:
        """
        raise NotImplementedError