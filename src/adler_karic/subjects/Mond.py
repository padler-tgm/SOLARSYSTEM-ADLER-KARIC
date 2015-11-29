from Planet import *


class Mond(Planet):
    def __init__(self, x, y, z, description, planet):
        Planet.__init__(self, x, y, z, description)
        self.orbit = (planet.orbit.attachNewNode('orbit_root_moon'))
        self.dayscale = 24
        self.yearscale = 687
        self.rspeed = 1.0
        self.tspeed = 1.0
        self.__init__texture()

    def __init__texture(self):
        self.texture = loader.loadModel("models/planet_sphere")
        self.texture.reparentTo(self.orbit)
        self.texture.setTexture(loader.loadTexture("models/moon_1k_tex.jpg"), 1)
        self.texture.setPos(self.position[0], self.position[1], self.position[2])
        self.texture.setScale(0.5 * self.scale)

    def chooseTexture(self):
        self.texture.setTexture(loader.loadTexture("models/moon_1k_tex.jpg"), 1)

    def setSpeed(self, rspeed, tspeed):
        if isinstance(rspeed, float):
            self.rspeed = rspeed
        if isinstance(tspeed, float):
            self.tspeed = tspeed
