from TruckAgent import Agent
from copy import copy

class Cell:
    def __init__(self, location, width, height, percept, direction, filled=False, endState=False, passable=False, 
                 visited=False, agent=Agent, goalFound=False):
        self.filled = filled
        self.endState = endState
        self.passable = passable
        self.location = location
        self.visited = visited
        self.width = width
        self.height = height
        self.percept = percept
        self.agent = agent
        self.direction = direction
        self.goalFound = goalFound

    def getDirection(self):
        return self.direction

    def setDirection(self, direction):
        self.direction = direction

    def getFilled(self):
        return self.filled

    def setFilled(self, filled):
        self.filled = filled
    
    def getEndstate(self):
        return self.endState
    
    def setEndstate(self, endState):
        self.endState = endState
        self.fillCell()
    
    def getPassable(self):
        return self.passable

    def setPassable(self, passable):
        self.passable = passable

    def getLocation(self):
        return self.location

    def setLocation(self, location):
        self.location = location

    def getVisited(self):
        return self.visited

    def setVisited(self, visited):
        self.visited = visited

    def getPercept(self):
        return self.percept

    def setPercept(self, percept):
        self.percept = percept

    def getAgent(self):
        return self.agent

    def setAgent(self, agent):
        self.agent = agent
    
    def getGoalFound(self):
        return self.goalFound

    def setGoalFound(self, goalFound):
        self.goalFound = goalFound

    def fillCell(self):
        if not self.passable:
            self.filled = True
            self.percept = 'NON_PASSABLE'
        elif self.endState:
            self.filled = True
            #self.buildEndState()
            precept = 'GOAL_CELL'

    # def buildEndState(self):

    #def buildArrow(self):

    def clone(self):
        cellClone = copy(self)
        cellClone.location = self.location
        cellClone.agent = self.agent
        return cellClone

    def equals(self, object):
        if object is None: return False

        if self is object: return True

        if not isinstance(object, Cell): return False

        if self.filled == object.filled and self.endState == object.endState and self.passable == object.passable and self.location == object.passable and self.visited == object.visited and self.width == object.width and self.height == object.height and self.direciton == object.direction and self.percept == object.percept:
            return True
        return False

    def toString(self):
        return "filled: " + self.filled + ", endState: " + self.endState + ", passable: " + self.passable + ", location: " + self.location + ", visited: " + self.visited + ", direction: " + self.direction