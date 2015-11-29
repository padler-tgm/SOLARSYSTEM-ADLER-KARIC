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

from subjects.Space import Space

#Generieren des Spielfelds
Space().createSpace()

#Sonne
sonne = Sonne(0, 0, 0, "sun")
sonne.setMoveBeharior(Rotation())
sonne.performMove()

#Merkur
merkur = Merkur(4, 0, 0, "mercury")
merkur.setMoveBeharior(Rotation())
merkur.setMoveBeharior(Translation())
merkur.performMove()

#Venus
venus = Venus(6.5, 0, 0, "venus")
venus.setMoveBeharior(Rotation())
venus.setMoveBeharior(Translation())
venus.performMove()

#Erde
erde = Erde(9, 0, 0, "earth")
erde.setMoveBeharior(Rotation())
erde.setMoveBeharior(Translation())
erde.performMove()

#Mond
mond = Mond(11, 0, 0, "moon", erde)
mond.setMoveBeharior(Rotation())
mond.setMoveBeharior(Translation())
mond.performMove()

#Mars
mars = Mars(13, 0, 0, "mars")
mars.setMoveBeharior(Rotation())
mars.setMoveBeharior(Translation())
mars.performMove()

#Jupiter
jupiter = Jupiter(17, 0, 0, "jupiter")
jupiter.setMoveBeharior(Rotation())
jupiter.setMoveBeharior(Translation())
jupiter.performMove()

#Saturn
saturn = Saturn(21, 0, 0, "saturn")
saturn.setMoveBeharior(Rotation())
saturn.setMoveBeharior(Translation())
saturn.performMove()

#Uranus
uranus = Uranus(25, 0, 0, "uranus")
uranus.setMoveBeharior(Rotation())
uranus.setMoveBeharior(Translation())
uranus.performMove()

#Neptun
neptun = Neptun(28, 0, 0, "neptune")
neptun.setMoveBeharior(Rotation())
neptun.setMoveBeharior(Translation())
neptun.performMove()

#Ausfuehren
run()
