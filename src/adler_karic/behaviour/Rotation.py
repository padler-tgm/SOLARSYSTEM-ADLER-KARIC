from Move import *
#from subjects import Planet

class Rotation(Move):
    def update(self, planet):
        #if isinstance(planet, Planet):
        planet.orbit_rotation = planet.orbit.hprInterval((0.241 * 60), Vec3(360, 0, 0)).loop()
        planet.day_rotation = planet.texture.hprInterval((59 * planet.dayscale), Vec3(360, 0, 0)).loop()
