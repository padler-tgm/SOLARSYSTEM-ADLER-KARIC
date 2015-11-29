from array import array
from abc import ABCMeta, abstractmethod
from behaviour.Move import Move
import direct.directbase.DirectStart
from panda3d.core import NodePath, TextNode, PointLight, VBase4
from direct.gui.DirectGui import *
from direct.showbase.DirectObject import DirectObject
import sys
from direct.task import Task
from math import pi, sin, cos


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
        self.h = False
        self.text = "Kamera: Maus\nAnimation start/stop: s\nAnimation schneller/langsamer: Mausrad rauf/runter\nTextur an/aus: t\nPunktlichtquelle setzen: Rechtsklick\nBeenden: Esc"
        self.tt = None
        self.t = True
        self.light = False
        self.plnp = None
        self.rspeed = 1.0
        self.tspeed = 1.0
        self.move = []


        base.setBackgroundColor(0, 0, 0)
        base.useDrive()
        #base.disableMouse()
        camera.setPos(0, 0, 45)
        camera.setHpr(0, -90, 0)
        self.createSpace()
        #self.accept("escape", sys.exit)
        #self.accept("mouse1", self.mouseListen)
        self.accept("h", self.showHelp) # help mit kommandos wird angezeigt (label)
        self.accept("escape", sys.exit) # programm wird beendet
        self.accept("t",self.texturAnAus) #textur an/aus
        self.accept("control-mouse1",self.changeLight) #punktlichtwuelle setzen
        self.accept("wheel_up",self.speedup) # animation wird schneller
        self.accept("wheel_down",self.speeddown) # animation wird langsamer
        self.accept("space",sys.exit)# animation stoppen und wieder startet
        #self.accept("mouse1", self.mouseListen) # im raum bewegen (maus halten)
        self.accept("space", self.startstop)  # animation stoppen und wieder startet
        #self.accept("mouse1", self.mouseListen) # im raum bewegen (maus halten)
        self.accept("a", self.camerapositionleftright)  # animation wird schneller
        self.accept("d", self.camerapositionleftright)  # animation wird langsamer
        #self.accept("control-mouse1", self.mouseListen)
        """self.accept("s",self.speed("s"))
        self.accept("f",self.speed("f"))"""

    def createSpace(self):
        self.sky = loader.loadModel("models/solar_sky_sphere")
        self.sky.reparentTo(render)
        self.sky.setScale(40)
        self.sky.setTexture(loader.loadTexture("models/stars_1k_tex.jpg"), 1)
        plight = PointLight('plight')
        plight.setColor(VBase4(0.8, 0.8, 0.8, 1))
        self.plnp = render.attachNewNode(plight)
        self.plnp.setPos(0, 0, 0)
        render.setLight(self.plnp)



    def changeLight(self):
        print("Hhhhh")
        if(self.light == True):
            self.light=False
            render.clearLight(self.plnp)
        else:
            self.light=True
            render.setLight(self.plnp)



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

    @abstractmethod
    def __init__texture(self):
        raise NotImplementedError

    def startstop(self):
        self.toggleInterval(self.rotation)
        if self.translation: self.toggleInterval(self.translation)

    def toggleInterval(self, interval):
        if interval.isPlaying(): interval.pause()
        else: interval.resume()

    def speedup(self):
        if(self.rspeed > 0.001):
            self.setSpeed(self.rspeed/10, self.tspeed/10)

    def speeddown(self):
        if(self.rspeed < 1):
            self.setSpeed(self.rspeed*10, self.tspeed*10)

    def camerapositionleftright(self):
        angleDegrees = self.scale * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        camera.setPos(20 * sin(angleRadians), -20.0 * cos(angleRadians), 3)
        camera.setHpr(angleDegrees, 0, 0)
        camera.lookAt(0,0,0)
        self.scale = self.scale + 1


    def cameraposition(self):
        pass
        #self.texture.setPos(0,42,0)
        #base.cam.reparentTo(render)
        #base.cam.setPos(30,-45,26)
        #base.cam.lookAt(0,0,0)
