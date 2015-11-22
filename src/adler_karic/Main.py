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

sonne = Sonne(0, 0, 0, "sun")
erde = Erde(8, 0, 0, "earth")
mond = Mond(9, 0, 0, "moon").setDependencie(erde)
merkur = Merkur(4,0,0,"mercury")
venus = Venus(6,0,0,"venus")
mars = Mars(10,0,0,"mars")
jupiter = Jupiter(12,0,0,"jupiter")
saturn = Saturn(14,0,0,"saturn")
uranus = Uranus(16,0,0,"uranus")
neptun = Neptun(18,0,0,"neptune")
run()
