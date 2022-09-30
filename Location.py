from copy import copy

class Location:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def setX(self, x):
        self.x = x

    def getX(self):
        return self.x

    def setY(self, y):
        self.y = y

    def getY(self):
        return self.y

    def toString(self):
        return "x: " + self.x + ", y: " + self.y

    def clone(self):
        return copy(self)
        
    def equals(self, o):
        if o == None:
            return False

        if self == o:
            return True

        if not isinstance(o, Location):
            return False

        if(self.x == o.x and self.y == o.y):
            return True

        return False


loc = Location(1, 2)
loc2 = loc.clone()
print(loc.equals(loc2))
loc.setX(5)
print(loc.equals(loc2))
print(loc.getX())
print(loc.getY())
