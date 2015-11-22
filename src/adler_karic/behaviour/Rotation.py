from Move import *


class Rotation(Move):
    def update(self, planet):
        planet.rotation = planet.texture.hprInterval((59 * planet.dayscale), Vec3(360, 0, 0))
        planet.rotation.loop()
