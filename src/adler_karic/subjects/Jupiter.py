from Planet import *
__author__ = 'Philipp Adler'
__author__ = 'Adin Karic'
__version__ = '2015-11-29'

class Jupiter(Planet):
    """
    Klasse fuer den Jupiter
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
        self.orbit = render.attachNewNode('orbit_root_jupiter')
        self.dayscale = 10
        self.yearscale = 11 * 365 + 315
        self.__init__texture()

    def __init__texture(self):
        """
        Methode bei der die Textur initialisert wird
        """
        self.texture = loader.loadModel("models/planet_sphere")
        self.texture.reparentTo(self.orbit)
        self.chooseTexture()
        self.texture.setPos(self.position[0], self.position[1], self.position[2])
        self.texture.setScale(1.5 * self.scale)

    def chooseTexture(self):
        """
        Methode zum Setzen der Ursprungstextur
        """
        self.texture.setTexture(loader.loadTexture("models/jupiter_1k_tex.jpg"), 1)