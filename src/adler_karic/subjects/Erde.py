from Planet import *
__author__ = 'Philipp Adler'
__author__ = 'Adin Karic'
__version__ = '2015-11-23'

class Erde(Planet):
    """
    Klasse fuer die Erde
    """
    def __init__(self, x, y, z, description):
        """
        Konstruktor der Klasse
        :param x: x-Position
        :param y: y-Position
        :param z: z-Position
        :param description: Beschreibung
        """
        Planet.__init__(self, x, y, z, description)
        self.orbit = render.attachNewNode('orbit_root_earth')
        self.dayscale = 24
        self.yearscale = 365
        self.__init__texture()

    def __init__texture(self):
        """
        Methode bei der die Textur initialisert wird
        """
        self.texture = loader.loadModel("models/planet_sphere")
        self.chooseTexture()
        self.texture.reparentTo(self.orbit)
        self.texture.setPos(self.position[0], self.position[1], self.position[2])
        self.texture.setScale(self.scale)

    def chooseTexture(self):
        """
        Methode zum Setzen der Ursprungstextur
        """
        self.texture.setTexture(loader.loadTexture("models/earth_1k_tex.jpg"), 1)

