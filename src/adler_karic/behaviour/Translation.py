from Move import *


class Translation(Move):
    def update(self, planet):
        print(planet.tspeed)
        planet.translation = planet.orbit.hprInterval(planet.yearscale*planet.tspeed, Vec3(360, 0, 0))
        planet.translation.loop()



