from array import array
from abc import ABCMeta, abstractmethod
from behaviour.Move import Move
import direct.directbase.DirectStart
from panda3d.core import NodePath
from direct.gui.DirectGui import *
from direct.showbase.DirectObject import DirectObject
import sys


class Planet(DirectObject):
    def __init__(self, x, y, z, description):
        self.position = array('d', [x,y,z])
        self.description = description
        self.orbit = None
        self.rotation = None
        self.translation = None
        self.scale = 1
        self.dayscale = None #Stunden
        self.yearscale = None #Tage
        self.texture = None
        self.rspeed = None
        self.tspeed = None
        self.move = []

        base.setBackgroundColor(0, 0, 0)
        #base.disableMouse()
        camera.setPos(0, 0, 45)
        camera.setHpr(0, -90, 0)
<<<<<<< HEAD
        self.createSpace()
        #self.accept("escape", sys.exit)
        #self.accept("mouse1", self.mouseListen)
=======
        self.accept("h",sys.exit) # help mit kommandos wird angezeigt (label)
        self.accept("escape", sys.exit) # programm wird beendet
        self.accept("t",sys.exit) #textur an/aus
        self.accept("mouse2",sys.exit) #punktlichtwuelle setzen
        self.accept("wheel_up",sys.exit) # animation wird schneller
        self.accept("wheel-down",sys.exit) # animation wird langsamer
        self.accept("s",sys.exit)# animation stoppen und wieder startet
        self.accept("mouse1", self.mouseListen) # im raum bewegen (maus halten)
        self.accept("control-mouse1", self.mouseListen)
        """self.accept("s",self.speed("s"))
        self.accept("f",self.speed("f"))"""
>>>>>>> 85f4d614e9354e908f0d29687e266c464fde26ae

    def createSpace(self):
        self.sky = loader.loadModel("models/solar_sky_sphere")
        self.sky.reparentTo(render)
        self.sky.setScale(40)
        self.sky.setTexture(loader.loadTexture("models/stars_1k_tex.jpg"), 1)
<<<<<<< HEAD
#        self.listener.accept(self,)
=======

>>>>>>> 85f4d614e9354e908f0d29687e266c464fde26ae

    def mouseListen(self):
        print("hehe")

    """def speed(self,str):
        if(str == "s"):
            print("gg")
        else:
            print("hh") """

    def performMove(self):
            for m in self.move:
                m.update(self)

    def setMoveBeharior(self, move):
        if isinstance(move, Move):
            self.move.append(move)

    def setSpeed(self, rspeed, tspeed):
        if isinstance(rspeed, float):
            self.rspeed = rspeed
        if isinstance(tspeed, float):
            self.tspeed = tspeed

    def setDependencie(self, planet):
        if isinstance(planet, Planet):
            self.orbit = (
                planet.orbit.attachNewNode('orbit_root_' + self.description))

    @abstractmethod
    def __init__texture(self):
        raise NotImplementedError
