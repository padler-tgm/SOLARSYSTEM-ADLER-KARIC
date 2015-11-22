from subjects.Sonne import Sonne
from subjects.Erde import Erde
from subjects.Mond import Mond

sonne = Sonne(0, 0, 0, "sun")
erde = Erde(10, 0, 0, "earth")
mond = Mond(15, 0, 0, "moon").setDependencie(erde)
run()
