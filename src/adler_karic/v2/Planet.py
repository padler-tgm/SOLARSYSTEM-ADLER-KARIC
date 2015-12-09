#from pandac.PandaModules import loadPrcFileData
#loadPrcFileData("", "want-directtools #t")
#loadPrcFileData("", "want-tk #t")
from math import pi, sin, cos
from panda3d.core import TextNode, GeomNode
from panda3d.core import CollisionTraverser,CollisionNode
from panda3d.core import CollisionHandlerQueue,CollisionRay
from panda3d.core import GeomVertexArrayFormat, GeomVertexFormat
from panda3d.core import Geom, GeomNode, GeomLines
from panda3d.core import GeomVertexReader, GeomVertexWriter
from panda3d.core import GeomVertexRewriter, GeomVertexData, PointLight, VBase4
from direct.gui.OnscreenText import OnscreenText
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
import random, sys, os, math
from Planetimpl import Planetimpl
from abc import abstractmethod

author = 'Philipp Adler'
author = 'Adin Karic'
version = '2015-11-29'
class Planet(ShowBase):
    #Macro-like function used to reduce the amount to code needed to create the
    #on screen instructions
    help=False
    text=None
    def genLabelText(self, text, i):
        """
        Generiert und erzeugt die Helpseite fuer unser Solarsystem
        :param text der angezeigte Text
        :param i: Position
        :return: die Bildschirmausgabe bzw. Helpseite
        """
        self.help = not self.help
        if(self.text != None):
            self.text.destroy()
        self.text= OnscreenText(text = text, pos = (-1.3, .95-.05*i), fg=(1,1,1,1),
                            align = TextNode.ALeft, scale = .05, mayChange = 1)
        return self.text

    def __init__(self, planeten):
        """
        Konstruktor hier wird alles gemanaget
        :param planeten: Planeten die erzeugt werden sollen
        """
        ShowBase.__init__(self)
        base.disableMouse()

        self.t = True

        # Pseudo-constants
        self.titleString = "Beste SolarSystem ever."
        self.renderRatio = 1.0e-6
        self.degPerSecond = 60.0
        self.minCameraDistance = 4.0
        self.maxCameraDistance = 4000.0
        self.zoomPerSecond = 1.8

        base.setBackgroundColor(0, 0, 0)

        # Init camera move variables
        self.keyMap = {"left":0, "right":0, "up":0, "down":0, "pageup":0, "pagedown":0, "wheelup":0, "wheeldown":0, "mouse3":0, "tab":0}
        self.angleLongitudeDegrees = 0.0
        self.angleLatitudeDegrees = 0.0
        self.cameraDistance = 10.0
        self.targetNode = render
        self.light = False

        #This code puts the standard title and instruction text on screen
        self.titleText = OnscreenText(text=self.titleString,
                                      style=1, fg=(1,1,0,1),
                                      pos=(0.8,-0.95), scale = .07)

        # Create empty node for world origin
        self.worldOrigin = render.attachNewNode("World Origin")
        self.planeten = planeten
        # Texture aender
        self.planeteninstance = []
        for p in planeten:
            if p[0] == "sun":
                self.su = Planetimpl(self.worldOrigin, 8.37800000E+06, 0, self.renderRatio, "sun", 10, 0)
                self.sun = self.su.impl()
                self.planeteninstance.extend([self.su])
                self.o = self.su
            else:
                self.o = Planetimpl(self.worldOrigin, p[1], p[2], self.renderRatio, p[0], p[3], p[4])
                self.orbit = self.o.impl()
                self.planeteninstance.extend([self.o])
            self.orbitOrbitVertexWriter = self.o.line()
            self.taskMgr.add(self.o.rotatePlanet, "rotate"+p[0], sort=1)
            self.taskMgr.add(self.o.translatePlanet, "move"+p[0]+"Orbit", sort=1)

        shadow = [[1.25, 1.25, 1.25]]
        self.plnp = []
        for s in shadow:
            self.plnp.append(self.pointlight(s[0], s[1], s[2]))
        # Attach the camera to the Earth to begin with
        self.targetNode = self.sun
        self.targetSize = float(self.targetNode.getTag("targetSize"))
        self.listener()
        self.cameraview()
        self.taskMgr.add(self.moveOrbitalCameraTask, "moveOrbitalCameraTask", sort=2)


    def pointlight(self, x, y, z):
        """
        Erzeugt einen Schatten, je nach Position der Sonne
        :return: die Schattierung des Planeten
        """
        plight = PointLight('plight')
        plight.setColor(VBase4(0.8, 0.8, 0.8, 1))
        plnp = render.attachNewNode(plight)
        plnp.setPos(x, y, z)
        return plnp


    def cameraview(self):
        """
        Cameraview
        """
        # Create picker Node and CollisionRay
        self.pickerNode = CollisionNode('mouseRay')
        self.pickerNP = camera.attachNewNode(self.pickerNode)
        self.pickerNode.setFromCollideMask(GeomNode.getDefaultCollideMask())
        self.pickerRay = CollisionRay()
        self.pickerNode.addSolid(self.pickerRay)

        # Create Collision Traverser and Queue
        self.cameraPickingTraverser = CollisionTraverser('Camera Picking Traverser')
        self.cameraPickingQueue = CollisionHandlerQueue()

        # Link Picker Node to Traverser and Queue
        self.cameraPickingTraverser.addCollider(self.pickerNP, self.cameraPickingQueue)

        # Set tags on Earth and Moon to be pickable

        # Add text to display the camera position
        self.text = OnscreenText(text = "Help: h", pos = (-1.3, .95-.05), fg=(1,1,1,1),align = TextNode.ALeft, scale = .05, mayChange = 1)
        """ self.displayCameraDistanceText = self.genLabelText("Camera distance : " + str(self.cameraDistance * self.planeten[0][1]) + " m", 0)
        self.displayCameraLatitudeText = self.genLabelText("Camera latitude : " + str(self.angleLatitudeDegrees) + " deg", 1)
        self.displayCameraLongitudeText = self.genLabelText("Camera longitude : " + str(self.angleLongitudeDegrees) + " deg", 2)
        self.displayTargetNodePositionText = self.genLabelText("Target position : (" + str(self.targetNode.getX()) + "; " + str(self.targetNode.getY()) + "; " + str(self.targetNode.getZ()) + ")", 3)
        self.help = False """

    def listener(self):
        """
        Hier werden alle Listener definiert
        """
        # Setup events for escape : exit from app
        self.accept("escape", sys.exit)


        self.accept("t", self.texturAnAus)  # textur an/aus
        self.accept("space", self.startstop)  # animation stoppen und wieder startet
        self.accept("w", self.speedup)  # animation wird schneller
        self.accept("s", self.speeddown)  # animation wird langsamer
        self.accept("l", self.changeLight)  # punktlichtwuelle setzen
        self.accept("h",self.showHelp) # Hilfe anzeigen lassen

        # Setup down events for arrow keys : rotating camera latitude and longitude
        self.accept("arrow_left", self.setKey, ["left",1])
        self.accept("arrow_right", self.setKey, ["right",1])
        self.accept("arrow_up", self.setKey, ["up",1])
        self.accept("arrow_down", self.setKey, ["down",1])

        # Setup up events for control keys
        self.accept("arrow_left-up", self.setKey, ["left",0])
        self.accept("arrow_right-up", self.setKey, ["right",0])
        self.accept("arrow_up-up", self.setKey, ["up",0])
        self.accept("arrow_down-up", self.setKey, ["down",0])

        # Setup events for mouse wheel
        self.accept("wheel_up", self.setKey, ["wheelup",1])
        self.accept("wheel_down", self.setKey, ["wheeldown",1])

        # Setup events for the Left Mouse Button : picking
        self.accept("mouse1", self.pickFromCamera)

        # Setup events for the Right Mouse Button : rotating camera latitude and longitude
        self.accept("mouse3", self.setKey, ["mouse3",1])
        self.accept("mouse3-up", self.setKey, ["mouse3",0])


    def changeLight(self):
        """
        Punktlichtquelle an/aus
        """
        if (self.light == True):
            self.light = False
            for p in self.plnp:
                render.clearLight(p)
        else:
            self.light = True
            for p in self.plnp:
                render.setLight(p)

    def texturAnAus(self):
        """
        Die bestehende Texture wird durch eine neue geaendert
        """
        if (self.t == True):
            self.t = False
            for p in self.planeteninstance:
                p.chooseTexture("models/borm.JPG")
        else:
            self.t = True
            for index, p in enumerate(self.planeteninstance):
                p.chooseTexture("models/"+self.planeten[index][0]+"_1k_tex.jpg")


    def startstop(self):
        """
        Startet oder stop den Weltraum
        """
        for index, p in enumerate(self.planeteninstance):
                if p.setstartstop():
                    self.taskMgr.add(p.rotatePlanet, "rotate"+self.planeten[index][0], sort=1)
                    self.taskMgr.add(p.translatePlanet, "move"+self.planeten[index][0]+"Orbit", sort=1)

    def showHelp(self):
        """
        Zeigt am Bildschirm die Bedienungsanleitung an oder nicht
        """
        if(self.help == True):
            self.help=False
            self.text.destroy()
            self.text = OnscreenText(text = "Help: h"
                                   , pos = (-1.3, .95-.05), fg=(1,1,1,1),
                       align = TextNode.ALeft, scale = .05, mayChange = 1)

        else:
            self.help=True
            if(self.text != None):
                self.text.destroy()
            self.text = OnscreenText(text = "Kamera: Maus\nAnimation start/stop: space\nAnimation schneller/langsamer: w/d\nTextur an/aus: t\nPunktlichtquelle setzen: l\nBeenden: Esc"
                                   , pos = (-1.3, .95-.05), fg=(1,1,1,1),
                       align = TextNode.ALeft, scale = .05, mayChange = 1)



    def speedup(self):
        """
        Erhoeht die Geschwindigkeit der Planet
        """
        for p in self.planeteninstance:
                p.rotation *= 10
                p.translation *= 10

    def speeddown(self):
        """
        Reduziert die Geschwindigkeit der Planet
        """
        for p in self.planeteninstance:
                p.rotation /= 10
                p.translation /= 10


    def pickFromCamera(self):
        """
        Erlaubt es einen Planeten anzuklicke um diesen zu vergrössern
        """
        mpos = base.mouseWatcherNode.getMouse()
        self.pickerRay.setFromLens(base.camNode, mpos.getX(), mpos.getY())

        self.cameraPickingTraverser.traverse(render)

        # Assume for simplicity's sake that myHandler is a CollisionHandlerQueue.
        if self.cameraPickingQueue.getNumEntries() > 0:
            # This is so we get the closest object.
            self.cameraPickingQueue.sortEntries()
            pickedObj = self.cameraPickingQueue.getEntry(0).getIntoNodePath()
            pickedObj = pickedObj.findNetTag('isPickable')
            if not pickedObj.isEmpty():
                self.targetNode = pickedObj
                self.targetSize = float(self.targetNode.getTag("targetSize"))

    def moveOrbitalCameraTask(self, task):
        """
        Define a procedure to move the camera.
        In fact, never moves the camera, but instead the world origin
        But always keeps the camera oriented towards the world origin
        :param task: Task
        :return: gibt einen Task zurueck der wiederholt ausgefuehrt wird
        """
        # Get mouse
        md = base.win.getPointer(0)
        x = md.getX()
        y = md.getY()



        if (self.keyMap["mouse3"]!=0):
            # Use mouse moves to change longitude and latitude
            self.angleLongitudeDegrees = self.angleLongitudeDegrees - (x - self.lastMouseX) * 0.2
            self.angleLatitudeDegrees = self.angleLatitudeDegrees - (y - self.lastMouseY) * 0.2
            # Restore position as frozen when the MB1 was depressed
            #base.win.movePointer(0, self.mouseFreezeX, self.mouseFreezeX)

        # Store latest mouse position for the next frame
        self.lastMouseX = x
        self.lastMouseY = y

        # First compute new camera angles and distance
        if (self.keyMap["left"]!=0):
            self.angleLongitudeDegrees = self.angleLongitudeDegrees - self.degPerSecond * globalClock.getDt()
        if (self.keyMap["right"]!=0):
            self.angleLongitudeDegrees = self.angleLongitudeDegrees + self.degPerSecond * globalClock.getDt()
        if (self.keyMap["up"]!=0):
            self.angleLatitudeDegrees = self.angleLatitudeDegrees - self.degPerSecond * globalClock.getDt()
        if (self.keyMap["down"]!=0):
            self.angleLatitudeDegrees = self.angleLatitudeDegrees + self.degPerSecond * globalClock.getDt()
        if (self.keyMap["wheelup"]!=0):
            self.cameraDistance = self.cameraDistance * (1 + (self.zoomPerSecond-1) * globalClock.getDt())
            self.setKey("wheelup",0)
        if (self.keyMap["wheeldown"]!=0):
            self.cameraDistance = self.cameraDistance / (1 + (self.zoomPerSecond-1) * globalClock.getDt())
            self.setKey("wheeldown",0)

        # Limit angles to [-180;+180]x[-90;+90] and distance between set min and max
        if (self.angleLongitudeDegrees > 180.0):
            self.angleLongitudeDegrees = self.angleLongitudeDegrees - 360.0
        if (self.angleLongitudeDegrees < -180.0):
            self.angleLongitudeDegrees = self.angleLongitudeDegrees + 360.0
        if (self.angleLatitudeDegrees > (90.0 - 0.001)):
            self.angleLatitudeDegrees = 90.0 - 0.001
        if (self.angleLatitudeDegrees < (-90.0 + 0.001)):
            self.angleLatitudeDegrees = -90.0 + 0.001
        if (self.cameraDistance < self.minCameraDistance):
            self.cameraDistance = self.minCameraDistance
        if (self.cameraDistance > self.maxCameraDistance):
            self.cameraDistance = self.maxCameraDistance

        # Convert to Radians
        angleLongitudeRadians = self.angleLongitudeDegrees * (pi / 180.0)
        angleLatitudeRadians = self.angleLatitudeDegrees * (pi / 180.0)

        # Compute the target object's position with respect to the camera
        x = -self.cameraDistance * self.targetSize * sin(angleLongitudeRadians) * cos(angleLatitudeRadians)
        y =  self.cameraDistance * self.targetSize * cos(angleLongitudeRadians) * cos(angleLatitudeRadians)
        z =  self.cameraDistance * self.targetSize * sin(angleLatitudeRadians)

        # Compute the world origin's position with respect to the camera
        x = (x * self.renderRatio) - self.targetNode.getX(self.worldOrigin)
        y = (y * self.renderRatio) - self.targetNode.getY(self.worldOrigin)
        z = (z * self.renderRatio) - self.targetNode.getZ(self.worldOrigin)

        # Apply the position
        self.worldOrigin.setPos(x, y, z)

        # Rotate the camera
        self.camera.setHpr(self.angleLongitudeDegrees, self.angleLatitudeDegrees, 0)

        # Display camera position
        """self.displayCameraDistanceText.setText("Camera distance : " + str(self.cameraDistance * self.targetSize) + " m")
        self.displayCameraLatitudeText.setText("Camera latitude : " + str(self.angleLatitudeDegrees) + " deg")
        self.displayCameraLongitudeText.setText("Camera longitude : " + str(self.angleLongitudeDegrees) + " deg")
        self.displayTargetNodePositionText.setText("Target position : (" + str(self.targetNode.getX()) + "; " + str(self.targetNode.getY()) + "; " + str(self.targetNode.getZ()) + ")")"""

        # End task
        return Task.cont

    #Records the state of the keyboard and mouse
    def setKey(self, key, value):
        """
        Mappt den Key mit einer Value
        :param key: Listener Key
        :param value: Value des Keys
        """
        # Store mouse position at the time of freeze
        if (key == "mouse3"):
            md = base.win.getPointer(0)
            self.lastMouseX = md.getX()
            self.lastMouseY = md.getY()
        #Store key/button press/release
        self.keyMap[key] = value
