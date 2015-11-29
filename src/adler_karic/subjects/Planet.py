from array import array
from abc import ABCMeta, abstractmethod
from behaviour.Move import Move
import direct.directbase.DirectStart
from panda3d.core import NodePath, TextNode, PointLight, VBase4
from direct.gui.DirectGui import *
from direct.showbase.DirectObject import DirectObject
from Space import Space
import sys

author = 'Philipp Adler'
author = 'Adin Karic'
version = '2015-11-29'
class Planet(DirectObject):
    """
    Planet stellt die Elternklasse fuer alle Planeten dar.
    Hier werden alle notwendigen Eigenschaften definiert.
    """
    def __init__(self, x, y, z, description):
        """
        Der Konstruktor erzeugt die Planeteigenschaften, wie die Position, Rotations- und Translationsgeschwindigkeit
        :param x: X-Koordinate des Planeten
        :param y: Y-Koordinate des Planeten
        :param z: Z-Koordinate des Planeten
        :param description: der Name des Planeten
        """
        self.position = array('d', [x, y, z])#Position des Planeten wird in einem Array gespeichert
        self.description = description
        self.orbit = None#beschreibt sich selber
        self.rotation = None#steuert die Rotation
        self.translation = None#steuert die Translatio
        self.scale = 1#Planetgroesse
        self.dayscale = None  #Anzahl der Stunden fuer eine vollstaendige Umdrehnung um sich selbst
        self.yearscale = None  #Anzahl der Tage fuer einen Umlauf um die Sonne
        self.texture = None#Texture
        self.rspeed = 0.1#Geschwindigkeit der Rotation
        self.tspeed = 0.1#Geschwindigkeit der Translation
        self.move = []#Hier wird gespeichert ob der Planet rotieren oder eine Translation vollfuehren soll
        self.h = False
        self.tt = None
        self.t = True
        self.light = False
        self.plnp = None

        base.setBackgroundColor(0, 0, 0)#schwarter Hintergrund
        base.useDrive()#Mouselistener
        camera.setPos(0, 0, 45)#Kameraposition
        camera.setHpr(0, -90, 0)#Kameraausrichtung
        self.plnp = Space().pointlight()
        self.showHelp()
        #Listener
        self.accept("h", self.showHelp) # help mit kommandos wird angezeigt (label)
        self.accept("escape", sys.exit) # programm wird beendet
        self.accept("t",self.texturAnAus) #textur an/aus
        self.accept("control-mouse1",self.changeLight) #punktlichtwuelle setzen
        self.accept("wheel_up",self.speedup) # animation wird schneller
        self.accept("wheel_down",self.speeddown) # animation wird langsamer
        self.accept("space", self.startstop)  # animation stoppen und wieder startet

    def changeLight(self):
        """
        Punktlichtquelle an/aus
        """
        if(self.light == True):
            self.light=False
            render.clearLight(self.plnp)
        else:
            self.light=True
            render.setLight(self.plnp)

    def showHelp(self):
        """
        Zeigt am Bildschirm die Bedienungsanleitung an oder nicht
        """
        if(self.h == True):
            self.h=False
            self.tt.destroy()
        else:
            self.h=True
            self.tt = OnscreenText(text = "Kamera: Maus\nAnimation start/stop: space\nAnimation schneller/langsamer: Mausrad rauf/runter\nTextur an/aus: t\nPunktlichtquelle setzen: Control-Rechtsklick\nBeenden: Esc"
                                   , pos = (-1.3, .95-.05), fg=(1,1,1,1),
                       align = TextNode.ALeft, scale = .05, mayChange = 1)


    def texturAnAus(self):
        """
        Die bestehende Texture wird durch eine neue geaendert
        """
        if(self.t == True):
            self.t = False
            self.texture.setTexture(loader.loadTexture("models/borm.JPG"), 1)
        else:
            self.t = True
            self.chooseTexture()

    def performMove(self):
        """
        Fuehrt je nach Einstellungen die Rotation und oder die Translation fuer den Planet aus
        """
        for m in self.move:
            m.update(self)

    def setMoveBeharior(self, move):
        """
        Hier wird definiert, ob sich der Planet drehen oder fortbewegene soll
        :param move: Ein Move Object, welches fuer die Rotation oder fuer die Translation zustaendig ist
        """
        if isinstance(move, Move):
            self.move.append(move)

    @abstractmethod
    def __init__texture(self):
        """
        Diese Methode muss von den expliziten Planeten implementiert werden.
        Definiert die jeweilige Texture
        """
        raise NotImplementedError

    def startstop(self):
        """
        Startet oder stop den Weltraum
        """
        self.toggleInterval(self.rotation)
        if self.translation: self.toggleInterval(self.translation)

    def toggleInterval(self, interval):
        """
        Hier werden die uebergebenen Objekte ueberprueft ob sich diese gerade bewegen oder still stehen.
        Falls sie sich bewegen werden sie gestoppt und anderfalls das Gegenteil
        :param interval: entweder Rotation oder Translation
        """
        if interval.isPlaying(): interval.pause()
        else: interval.resume()

    def speedup(self):
        """
        Erhoeht die Geschwindigkeit der Planet
        """
        if(self.rspeed > 0.001):
            self.rspeed = self.rspeed/4
            self.performMove()

    def speeddown(self):
        """
        Reduziert die Geschwindigkeit der Planet
        """
        if(self.rspeed < 1):
            self.rspeed = self.rspeed*4
            self.performMove()
