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
#groesse ist volumen bei planeten
from behaviour.Translation import Translation

sonne = Sonne(0, 0, 0, "sun")
sonne.setMoveBeharior(Rotation())
sonne.performMove()

merkur = Merkur(4, 0, 0, "mercury")
merkur.setMoveBeharior(Rotation())
sonne.setMoveBeharior(Translation())
merkur.performMove()

venus = Venus(6.5, 0, 0, "venus")
venus.setMoveBeharior(Rotation())
venus.performMove()

erde = Erde(9, 0, 0, "earth")
erde.setMoveBeharior(Rotation())
erde.performMove()

mond = Mond(11, 0, 0, "moon")
mond.setDependencie(erde)
mond.setMoveBeharior(Rotation())
mond.performMove()

mars = Mars(13, 0, 0, "mars")
mars.setMoveBeharior(Translation())
mars.performMove()

jupiter = Jupiter(17, 0, 0, "jupiter")
jupiter.setMoveBeharior(Rotation())
jupiter.performMove()

saturn = Saturn(21, 0, 0, "saturn")
saturn.setMoveBeharior(Rotation())
saturn.performMove()

uranus = Uranus(25, 0, 0, "uranus")
uranus.setMoveBeharior(Rotation())
uranus.performMove()

neptun = Neptun(28, 0, 0, "neptune")
neptun.setMoveBeharior(Rotation())
neptun.performMove()

run()
