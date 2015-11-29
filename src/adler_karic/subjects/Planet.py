from array import array
from abc import ABCMeta, abstractmethod
from behaviour.Move import Move
import direct.directbase.DirectStart
from panda3d.core import NodePath, TextNode, PointLight, VBase4
from direct.gui.DirectGui import *
from direct.showbase.DirectObject import DirectObject



class Planet(DirectObject):
    def __init__(self, x, y, z, description):
        self.position = array('d', [x, y, z])
        self.description = description
        self.orbit = None
        self.rotation = None
        self.translation = None
        self.scale = 1
        self.dayscale = None  # Stunden
        self.yearscale = None  # Tage
        self.texture = None
        self.rspeed = 1.0
        self.tspeed = 1.0
        self.move = []
        base.setBackgroundColor(0, 0, 0)
        base.useDrive()
        camera.setPos(0, 0, 45)
        camera.setHpr(0, -90, 0)
        camera.lookAt(0,0,0)

    def performMove(self):
        for m in self.move:
            m.update(self)

    def setMoveBeharior(self, move):
        if isinstance(move, Move):
            self.move.append(move)

    @abstractmethod
    def __init__texture(self):
        raise NotImplementedError

    def texturAnAus(self):
        if (self.t == True):
            self.t = False
            self.texture.setTexture(loader.loadTexture("models/borm.JPG"), 1)
        else:
            self.t = True
            self.chooseTexture()
