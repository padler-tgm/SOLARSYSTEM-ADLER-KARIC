from Planet import Planet


class Sonne(Planet):
    def __init__(self, x, y, z, description):
        Planet.__init__(self, x, y, z, description)
        self.orbit = render.attachNewNode('orbit_root_sun')
        self.dayscale = 24
        self.rspeed = 1.0
        self.tspeed = 0
        self.__init__texture()

    def __init__texture(self):
        self.texture = loader.loadModel("models/planet_sphere")
        self.texture.reparentTo(self.orbit)
        self.texture.setTexture(loader.loadTexture("models/sun_1k_tex.jpg"), 1)
        self.texture.setPos(self.position[0], self.position[1], self.position[2])
        self.texture.setScale(2.5*self.scale)

    def chooseTexture(self):
        self.texture.setTexture(loader.loadTexture("models/sun_1k_tex.jpg"), 1)

    def setSpeed(self, rspeed, tspeed):
        if isinstance(rspeed, float):
            self.rspeed = rspeed
        if isinstance(tspeed, float):
            self.tspeed = tspeed
        self.performMove()
