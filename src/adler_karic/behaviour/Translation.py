from Move import *


class Translation(Move):
    def update(self, planet):
        planet.orbit.hprInterval(planet.yearscale, Vec3(360, 0, 0)).loop()
