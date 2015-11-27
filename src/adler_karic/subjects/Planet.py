from array import array
from abc import ABCMeta, abstractmethod
from behaviour.Move import Move
import direct.directbase.DirectStart
from panda3d.core import NodePath, TextNode
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
        self.h = False
        self.text = "Kamera: Maus\nAnimation start/stop: s\nAnimation schneller/langsamer: Mausrad rauf/runter\nTextur an/aus: t\nPunktlichtquelle setzen: Rechtsklick\nBeenden: Esc"
        self.tt = None
        self.t = True

        self.move = []

        base.setBackgroundColor(0, 0, 0)
        #base.disableMouse()
        camera.setPos(0, 0, 45)
        camera.setHpr(0, -90, 0)
        self.createSpace()
        #self.accept("escape", sys.exit)
        #self.accept("mouse1", self.mouseListen)
        self.accept("h", self.showHelp) # help mit kommandos wird angezeigt (label)
        self.accept("escape", sys.exit) # programm wird beendet
        self.accept("t",self.texturAnAus) #textur an/aus
        self.accept("mouse2",sys.exit) #punktlichtwuelle setzen
        self.accept("wheel_up",sys.exit) # animation wird schneller
        self.accept("wheel-down",sys.exit) # animation wird langsamer
        self.accept("s",sys.exit)# animation stoppen und wieder startet
        self.accept("mouse1", self.mouseListen) # im raum bewegen (maus halten)
        self.accept("control-mouse1", self.mouseListen)
        """self.accept("s",self.speed("s"))
        self.accept("f",self.speed("f"))"""

    def createSpace(self):
        self.sky = loader.loadModel("models/solar_sky_sphere")
        self.sky.reparentTo(render)
        self.sky.setScale(40)
        self.sky.setTexture(loader.loadTexture("models/stars_1k_tex.jpg"), 1)

    def showHelp(self):
        if(self.h == True):
            self.h=False
            self.tt.destroy()

        else:
            self.h=True
            self.tt = OnscreenText(text = self.text, pos = (-1.3, .95-.05), fg=(1,1,1,1),
                       align = TextNode.ALeft, scale = .05, mayChange = 1)
    def texturAnAus(self):
        if(self.t == True):
            self.t = False
            self.texture.setTexture(loader.loadTexture("models/borm.JPG"), 1)
        else:
            self.t = True
            self.chooseTexture()
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

"""
    @abstractmethod
    def chooseTexture(self):

        raise NotImplementedError """
