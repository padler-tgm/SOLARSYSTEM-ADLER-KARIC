from math import pi, sin, cos
from panda3d.core import TextNode, GeomNode
from panda3d.core import CollisionTraverser,CollisionNode
from panda3d.core import CollisionHandlerQueue,CollisionRay
from panda3d.core import GeomVertexArrayFormat, GeomVertexFormat
from panda3d.core import Geom, GeomNode, GeomLines
from panda3d.core import GeomVertexReader, GeomVertexWriter
from panda3d.core import GeomVertexRewriter, GeomVertexData
from direct.gui.OnscreenText import OnscreenText
from direct.task import Task

class Planetimpl():
    def __init__(self, world, size, distance, ratio, description, rotation, translation):
        self.worldOrigin = world
        self.size = size
        self.distance = distance
        self.renderRatio = ratio
        self.description = description
        self.rotation = rotation
        self.translation = translation

    def impl(self):
        # Load the Moon model
        self.planet = loader.loadModel("models/planet_sphere")
        self.chooseTexture("models/"+self.description+"_1k_tex.jpg")
        self.planet.reparentTo(self.worldOrigin)
        self.planet.setScale(self.size * self.renderRatio)
        self.planet.setPos(self.distance * self.renderRatio, 0.0, 0.0)
        self.planet.setTag('targetSize', str(self.size))
        self.planet.setTag('isPickable', '2')
        self.startstop = True
        return self.planet

    def chooseTexture(self, name):
        """
        Methode zum Setzen der Ursprungstextur
        """
        self.planet.setTexture(loader.loadTexture(name), 1)

    def line(self):
        # Create and populate the Moon orbit model using Vertices and Lines
        self.planetOrbitVertexData = GeomVertexData(self.description+'OrbitVertexData', GeomVertexFormat.getV3(), Geom.UHDynamic)
        self.planetOrbitVertexWriter = GeomVertexWriter(self.planetOrbitVertexData, 'vertex')
        self.planetOrbitNumberPoints = 360
        for i in range(self.planetOrbitNumberPoints):
            angleDegrees = i * 360 / self.planetOrbitNumberPoints
            angleRadians = angleDegrees * (pi / 180.0)
            x = -self.distance * sin(angleRadians)
            y =  self.distance * cos(angleRadians)
            self.planetOrbitVertexWriter.addData3f(x, y, 0.0)
        self.planetOrbitLines = GeomLines(Geom.UHStatic)
        for i in range(self.planetOrbitNumberPoints-1):
            self.planetOrbitLines.addVertex(i)
            self.planetOrbitLines.addVertex(i+1)
            self.planetOrbitLines.closePrimitive()
            self.planetOrbitLines.addVertex(self.planetOrbitNumberPoints-1)
            self.planetOrbitLines.addVertex(0)
        self.planetOrbitLines.closePrimitive()
        self.planetOrbitGeom = Geom(self.planetOrbitVertexData)
        self.planetOrbitGeom.addPrimitive(self.planetOrbitLines)
        self.planetOrbitNode = GeomNode(self.description+'OrbitNode')
        self.planetOrbitNode.addGeom(self.planetOrbitGeom)
        self.planetOrbitNnodePath = render.attachNewNode(self.planetOrbitNode)
        self.planetOrbitNnodePath.reparentTo(self.worldOrigin)
        return self.planetOrbitVertexWriter

    def setstartstop(self):
        self.startstop = not self.startstop
        return self.startstop

    def rotatePlanet(self, task):
        # Compute earth rotation
        frameTime = globalClock.getFrameTime()
        angleDegrees = frameTime *  self.rotation
        self.planet.setHpr(angleDegrees, 0, 0)
        # End task
        if self.startstop:
            return Task.cont
        else:
            return Task.done



    def translatePlanet(self, task):
        # Compute Moon position relative to Earth with circular orbit
        frameTime = globalClock.getFrameTime()
        angleDegrees = frameTime *  self.translation
        angleRadians = angleDegrees * (pi / 180.0)

        # Compute the Moon's position with respect to the Earth
        x = -self.distance * self.renderRatio * sin(angleRadians)
        y =  self.distance * self.renderRatio * cos(angleRadians)

        # Set the position on the model
        self.planet.setPos(x, y, 0.0)

        # Also rotate the orbit to follow the Moon and eliminate jitter effect
        self.planetOrbitVertexWriter.setRow(0)
        for i in range(self.planetOrbitNumberPoints):
            angleDegrees = angleDegrees + 360.0 / self.planetOrbitNumberPoints
            angleRadians = angleDegrees * (pi / 180.0)
            x = -self.distance * self.renderRatio * sin(angleRadians)
            y =  self.distance * self.renderRatio * cos(angleRadians)
            self.planetOrbitVertexWriter.setData3f(x, y, 0.0)

        # End task
        if self.startstop:
            return Task.cont
        else:
            return Task.done