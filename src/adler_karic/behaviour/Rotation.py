from Move import *


class Rotation(Move):
    def update(self, planet):
        planet.rotation = planet.texture.hprInterval((planet.dayscale*planet.rspeed), Vec3(360, 0, 0))
        planet.rotation.loop()

