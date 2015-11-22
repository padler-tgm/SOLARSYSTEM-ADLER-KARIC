from subjects.Sonne import Sonne
from subjects.Erde import Erde
from subjects.Mond import Mond
from subjects.Merkur import Merkur
from subjects.Venus import Venus
from subjects.Mars import Mars
from subjects.Jupiter import Jupiter
from subjects.Saturn import Saturn
from subjects.Uranus import Uranus
from subjects.Neptun import Neptun
from behaviour.Rotation import Rotation

sonne = Sonne(0, 0, 0, "sun")
sonne.setMoveBeharior(Rotation())
sonne.performMove()

erde = Erde(8, 0, 0, "earth")
erde.setMoveBeharior(Rotation())
erde.performMove()

mond = Mond(9, 0, 0, "moon").setDependencie(erde)
mond = Mond(15, 0, 0, "moon")
mond.setDependencie(erde)
mond.setMoveBeharior(Rotation())
mond.performMove()

merkur = Merkur(4, 0, 0, "mercury")
merkur.setMoveBeharior(Rotation())
merkur.performMove()

venus = Venus(6, 0, 0, "venus")
venus.setMoveBeharior(Rotation())
venus.performMove()

mars = Mars(10, 0, 0, "mars")
mars.setMoveBeharior(Rotation())
mars.performMove()

jupiter = Jupiter(12, 0, 0, "jupiter")
jupiter.setMoveBeharior(Rotation())
jupiter.performMove()

saturn = Saturn(14, 0, 0, "saturn")
saturn.setMoveBeharior(Rotation())
saturn.performMove()

uranus = Uranus(16, 0, 0, "uranus")
uranus.setMoveBeharior(Rotation())
uranus.performMove()

neptun = Neptun(18, 0, 0, "neptune")
neptun.setMoveBeharior(Rotation())
neptun.performMove()

run()
