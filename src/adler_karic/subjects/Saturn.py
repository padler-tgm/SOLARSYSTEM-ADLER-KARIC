from Planet import *


class Saturn(Planet):
    def __init__(self, x, y, z, description):
        Planet.__init__(self, x, y, z, description)
        self.orbit = render.attachNewNode('orbit_root_saturn')
        self.__init__texture()

    def __init__texture(self):
        self.texture = loader.loadModel("models/planet_sphere")
        self.texture.reparentTo(self.orbit)
        self.texture.setTexture(loader.loadTexture("models/saturn_1k_tex.jpg"), 1)
        self.texture.setPos(self.position[0], self.position[1], self.position[2])
        self.texture.setScale(1/11.4 * self.scale)