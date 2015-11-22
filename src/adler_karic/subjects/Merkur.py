from Planet import *


class Merkur(Planet):
    def __init__(self, x, y, z, description):
        Planet.__init__(self, x, y, z, description)
        self.orbit = render.attachNewNode('orbit_root_mercury')
        self.__init__texture()

    def __init__texture(self):
        self.texture = loader.loadModel("models/planet_sphere")
        self.texture.reparentTo(self.orbit)
        self.texture.setTexture(loader.loadTexture("models/mercury_1k_tex.jpg"), 1)
        self.texture.setPos(self.position[0], self.position[1], self.position[2])
        self.texture.setScale(1/277 * self.scale)