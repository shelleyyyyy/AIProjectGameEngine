from Location import Location
from copy import copy

class TruckAgent:
    def __init__(self):
        self.agentId
        self.movable = False
        self.direction = "FACING_WEST"
        self.location = Location

    def setUUID(self, agentId):
        self.agentId = agentId

    def getUUID(self):
        return self.getUUID

    def setMovable(self, movable):
        self.movable = movable

    def getMovable(self):
        return self.movable

    def setDirection(self, direction):
        self.direction = direction

    def getDirection(self):
        return self.direction

    def setLocation(self, location):
        self.location = location

    def getLocation(self): 
        return self.location

    # FLIP TRUCK

    def clone(self):
        truckAgentClone = self.clone()
        truckAgentClone.location = self.location.clone()

        return truckAgentClone

    def toString(self):
        return "Agent ID: " + self.getUUID() + ", x = " + self.getLocation().getX() + ", y = " + self.getLocation().getY()

