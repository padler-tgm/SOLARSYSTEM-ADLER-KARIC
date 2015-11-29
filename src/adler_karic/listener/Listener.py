from direct.showbase.DirectObject import DirectObject
from direct.gui.DirectGui import *
import direct.directbase.DirectStart
from panda3d.core import NodePath, TextNode, PointLight, VBase4
import sys


class Listener(DirectObject):
    def __init__(self):
        self.createlistener()
        self.h = False
        self.tt = None
        self.t = True
        self.light = False
        self.plnp = None
        plight = PointLight('plight')
        plight.setColor(VBase4(0.8, 0.8, 0.8, 1))
        self.plnp = render.attachNewNode(plight)
        self.plnp.setPos(0, 0, 0)

    def createlistener(self):
        self.accept("h", self.showHelp)  # help mit kommandos wird angezeigt (label)
        self.accept("escape", sys.exit)  # programm wird beendet
        self.accept("t", Planet.texturAnAus)  # textur an/aus
        self.accept("control-mouse1", self.changeLight)  # punktlichtwuelle setzen
        self.accept("wheel_up", self.speedup)  # animation wird schneller
        self.accept("wheel_down", self.speeddown)  # animation wird langsamer
        self.accept("space", self.startstop)  # animation stoppen und wieder startet

    def showHelp(self):
        if (self.h == True):
            self.h = False
            self.tt.destroy()
        else:
            self.h = True
            self.tt = OnscreenText(
                text="Kamera: Maus\nAnimation start/stop: space\nAnimation schneller/langsamer: Mausrad rauf/runter\nTextur an/aus: t\nPunktlichtquelle setzen: Control-Rechtsklick\nBeenden: Esc"
                , pos=(-1.3, .95 - .05), fg=(1, 1, 1, 1),
                align=TextNode.ALeft, scale=.05, mayChange=1)

    def changeLight(self):
        if (self.light == True):
            self.light = False
            render.clearLight(self.plnp)
        else:
            self.light = True
            render.setLight(self.plnp)

    def speedup(self):
        if (self.rspeed > 0.001):
            self.rspeed = self.rspeed / 4
            self.performMove()

    def speeddown(self):
        if (self.rspeed < 1):
            self.rspeed = self.rspeed * 4
            self.performMove()

    def startstop(self):
        self.toggleInterval(self.rotation)
        if self.translation: self.toggleInterval(self.translation)

    def toggleInterval(self, interval):
        if interval.isPlaying():
            interval.pause()
        else:
            interval.resume()
