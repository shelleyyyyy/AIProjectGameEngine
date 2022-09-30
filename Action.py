
from asyncio import constants
from asyncio.windows_events import NULL
from platform import platform

import Constants, math
class Action(Constants):
    GO_FORWARD_STEP_COST = 1
    TURN_LEFT_STEP_COST = 1
    TURN_RIGHT_STEP_COST = 1
    GO_FORWARD = 'goForward'
    TURN_LEFT = 'goLeft'
    TURN_RIGHT = 'goRight'
    
    def __init__(self):
        super().__init__()
        
        
    
    def getStepCost(self,action):
        if action == self.GO_FORWARD:
            return self.GO_FORWARD_STEP_COST
        elif action == self.TURN_RIGHT:
            return self.TURN_RIGHT_STEP_COST
        elif action == self.TURN_LEFT:
            return self.TURN_LEFT_STEP_COST


    def goForward(self,enviroment, agent):
        shiftXValue = 0
        shiftYValue = 0

        # if agent.getDirection() == FACING_SOUTH:
        #     shiftXValue=MOVING_SOUTH
        # elif agent.getDirection() == FACING_WEST:
        #     shiftYValue = MOVING_WEST
        # elif agent.getDirection() == FACING_NORTH:
        #     shiftXValue = MOVING_NORTH
        # elif agent.getDirection() == FACING_EAST:
        #     shiftYValue = MOVING_EAST
        
        # oldX = agent.getLocation().getX()
        # oldY = agent.getLocation().getY()

        # i = agent.getLocation().getX() + shiftXValue
        # j = agent.getLocation().getY() + shiftYValue

        # if i < 0 or i > len(enviroment.getAgents()) or j < 0 or len(enviroment.getAgents()):
        #     return False
        
        # if enviroment.getCells()[i][j].getPassable():
        #     enviroment.getAgents()[oldX][oldY] = agent
        #     enviroment.getChildren().remove(agent)

        #     enviroment.getCells()[i][j].getChildren().add(agent)
        #     enviroment.getCells()[oldX][oldY].setAgent(NULL)
        #     enviroment.getCells()[i][j].setAgent(agent)

        #     enviroment.getCells()[oldX][oldY].setVisited(True)
           


        #     agent.getLocation().setX(i)
        #     agent.getLocation().setY(j)

        return True



    
    def turnRight(self,agent):
        pass


    def turnLeft(self,agent):
        pass
    