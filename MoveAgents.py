import abc, Action
class MoveAgents(Action):
    def __init__(self, enviroment, agents, perceptsOfCells, truckCounter, searchType, waitTime, maxStep, maxTime):
        self.enviroment = enviroment
        self.agents = agents
        self.perceptsOfCells = perceptsOfCells
        self.truckCounter = truckCounter
        self.searchType = searchType
        self.waitTime = waitTime
        self.maxStep = maxStep
        self.maxTime = maxTime
        

    pass
