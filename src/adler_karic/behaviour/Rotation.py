from Move import *

author = 'Philipp Adler'
author = 'Adin Karic'
version = '2015-11-29'
class Rotation(Move):
    """
    In dieser Klasse rotiert der Planet um seine eigene Achse
    """
    def update(self, planet):
        """
        Laesst den Planet je nach Einstellung unterschiedlich schnell rotieren
        :param planet: der uebergebene Planet wird rotieren
        """
        planet.rotation = planet.texture.hprInterval((planet.dayscale*planet.rspeed), Vec3(360, 0, 0))
        planet.rotation.loop()

