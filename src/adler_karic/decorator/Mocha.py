import CondimentDecorator

class Mocha(CondimentDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def getMove(self):
        return self.beverage.getMove() + "Translation"