from direct.showbase.DirectObject import DirectObject
class Listener(DirectObject):
    def __init__(self):
        self.accept("mouse1",self.mlisten())

    def mlisten(self):
        print("adin")