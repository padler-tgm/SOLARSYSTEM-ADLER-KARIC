from Planet import *


class Uranus(Planet):
    def __init__(self, x, y, z, description):
        Planet.__init__(self, x, y, z, description)
        self.__init__texture()

    def __init__texture(self):
        self.texture = loader.loadModel("models/planet_sphere")
        self.texture.reparentTo(render)
        self.texture.setTexture(loader.loadTexture("models/uranus_1k_tex.jpg"), 1)
        self.texture.setPos(self.position[0], self.position[1], self.position[2])
        self.texture.setScale(1.5 * self.scale)
