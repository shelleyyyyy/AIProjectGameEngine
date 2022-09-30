from TruckAgent import Agent
from copy import deepcopy

class Cell:
    def __init__(self, location, width, height, percept, direction, filled=False, endState=False, passable=False, 
                 visited=False, agent=Agent, goalFound=False):
        self.__filled = filled
        self.__endState = endState
        self.__passable = passable
        self.__location = location
        self.__visited = visited
        self.__width = width
        self.__height = height
        self.__percept = percept
        self.__agent = agent
        self.__direction = direction
        self.__goalFound = goalFound

    def getDirection(self):
        return self.__direction

    def setDirection(self, direction):
        self.__direction = direction

    def getFilled(self):
        return self.__filled

    def setFilled(self, filled):
        self.__filled = filled
    
    def getEndstate(self):
        return self.__endState
    
    def setEndstate(self, endState):
        self.__endState = endState
        self.fillCell()
    
    def getPassable(self):
        return self.__passable

    def setPassable(self, passable):
        self.__passable = passable

    def getLocation(self):
        return self.__location

    def setLocation(self, location):
        self.__location = location

    def getVisited(self):
        return self.__visited

    def setVisited(self, visited):
        self.__visited = visited

    def getPercept(self):
        return self.__percept

    def setPercept(self, percept):
        self.__percept = percept

    def getAgent(self):
        return self.__agent

    def setAgent(self, agent):
        self.__agent = agent
    
    def getGoalFound(self):
        return self.__goalFound

    def setGoalFound(self, goalFound):
        self.__goalFound = goalFound

    def fillCell(self):
        if not self.__passable:
            self.__filled = True
            self.__percept = 'NON_PASSABLE'
        elif self.__endState:
            self.__filled = True
            #self.buildEndState()
            precept = 'GOAL_CELL'

    # def buildEndState(self):

    #def buildArrow(self):

    def clone(self):
        cellClone = deepcopy(self)
        cellClone.location = self.__location
        cellClone.agent = self.__agent
        return cellClone

    def equals(self, object):
        if object is None: return False

        if self is object: return True

        if not isinstance(object, Cell): return False

        if (self.__filled == object.filled and self.__endState == object.endState and
            self.__passable == object.passable and self.__location == object.passable and
            self.__visited == object.visited and self.__width == object.width and
            self.__height == object.height and self.__direciton == object.direction and
            self.__percept == object.percept):
            return True
        return False

    def toString(self):
        return ("filled: " + self.__filled + ", endState: " + self.__endState + ", passable: " +
                self.__passable + ", location: " + self.__location + ", visited: " + 
                self.__visited + ", direction: " + self.__direction)