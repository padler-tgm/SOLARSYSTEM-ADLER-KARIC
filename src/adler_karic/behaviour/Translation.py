from Move import *

author = 'Philipp Adler'
author = 'Adin Karic'
version = '2015-11-29'
class Translation(Move):
    def update(self, planet):
        """
        Unterschiedliche Geschwindigkeit bei der Translation je nach Einstellungen
        :param planet: der uebergebene Planet fuehrt eine Translation aus
        """
        planet.translation = planet.orbit.hprInterval(planet.yearscale*planet.tspeed, Vec3(360, 0, 0))
        planet.translation.loop()



