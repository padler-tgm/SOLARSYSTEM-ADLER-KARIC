from Move import *


class Translation(Move):
    def update(self, planet):
        planet.translation = planet.orbit.hprInterval(planet.yearscale*planet.tspeed, Vec3(360, 0, 0))
        planet.translation.loop()



