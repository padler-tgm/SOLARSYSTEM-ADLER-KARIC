import direct.directbase.DirectStart
from panda3d.core import NodePath, TextNode, PointLight, VBase4, Point3
from direct.gui.DirectGui import *
from direct.showbase.DirectObject import DirectObject

author = 'Philipp Adler'
author = 'Adin Karic'
version = '2015-11-29'
class Space:
    """
    Definiert ein Spielfeld wo die Planeten erzeugt werden
    """
    def createSpace(self):
        """
        Generiert das Spielfeld mit Sternen im Hintergrund
        """
        self.sky = loader.loadModel("models/solar_sky_sphere")
        self.sky.reparentTo(render)
        self.sky.setScale(40)
        self.sky.setTexture(loader.loadTexture("models/stars_1k_tex.jpg"), 1)

    def pointlight(self, x,y,z):
        """
        Erzeugt einen Schatten, je nach Position der Sonne
        :return: die Schattierung des Planeten
        """
        plight = PointLight('plight')
        plight.setColor(VBase4(0.8, 0.8, 0.8, 1))
        plnp = render.attachNewNode(plight)
        plnp.setPos(x, y, z)
        return plnp