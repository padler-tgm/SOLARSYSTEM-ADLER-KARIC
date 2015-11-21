import array

from behaviour import Move


class Planet():
    def __init__(self,x,y,z):
        self.position = array(x,y,z)
        self.size = None
        self.texture = None
        self.abhplanet = None
        self.rspeed = None
        self.tspeed = None
        self.move = None
        self.zeit = None

    def performMove(self):
        if isinstance(self.move, Move):
            self.move.update(self)

    def setMoveBeharior(self,move):
        if isinstance(self.move, Move):
            self.move = move

    def setSpeed(self,rspeed,tspeed):
        if isinstance(rspeed,float):
            self.rspeed = rspeed
        if isinstance(tspeed,float):
            self.tspeed = tspeed

    def setDependencie(self,planet):
        if isinstance(planet,Planet):
            self.abhplanet = planet

    def __init__texture(self):
        pass