from Location import Location
from TruckAgent import TruckAgent
import random
from Cell import Cell

class enviroment:
    width, height = (10, 10)

    def __init__(self, num_of_agents = 0, num_of_goals = 0, num_of_non_passable = 0):
        self.num_of_agents = num_of_agents
        self.num_of_goals = num_of_goals
        self.num_of_non_passable = num_of_non_passable
        self.cells

    def create_grid(self):
        env = [[0] * self.width] * self.height
        print(env)
        print(self.num_of_agents)
    
    #returns an array of TruckAgents
    def fill_cells(num_of_agents, num_obstacles):
        for i in range(len(grid_size)):
            for j in range(len(grid_size[i])):
                location = Location()
                cell = Cell(location=Location(i, j), width=width_of_cell, height=hieght_of_cell, 
                percept=BLANK, direction=Constants.FACING_WEST)
                this.add(cell, j, i) #unsure what this is in reference too
                cells[i][j] = cell
            
        createObstacles(num_obstacles)

        return createAgents(num_of_agents)

    
    def createAgents(num_of_agents):
        trucks = []

        widthOfSingleCell = width / grid_size
        heightOfSingleCell = height / grid_size
        count = 0

        while(count < num_of_agents):
            i = random.randint(0, grid_size)
            j = random.randint(0, grid_size)

            if cells[i][j].getPassable(): #getPassable needs to implamented
                truck = TruckAgent()
                agent[i][j] = truck
                cells[i][j].getChildren.add(truck) #getChildren and add() needs to be implamented
                cells[i][j].setVisited(True) #check on setVisted()
                cells[i][j].setAgent(truck) #check on setAgent
                trucks[count] = truck
                count+= 1
                cells[i][j].setPassable(False) #check setPassable()

            return trucks

    def createObstacles(num_obstacles):
        count = 0
        while count < num_obstacles:
            i = random.randint(0, grid_size)
            j = random.randint(0, grid_size)

            if cells[i][j].getPassable():
                cell = Cell(location=Location(i, j), width=width_of_cell, 
                height=hieght_of_cell, percept=NON_PASSABLE, 
                direction=Constants.FACING_WEST)

                cell.setPassable(False)
                cell.fillCell()
                this.add(cell, j, i) #not sure what this.add is in reference too
                count+=1
            
    def createGoals(num_of_goals):
        goals = []
        count = 0

        while count < num_obstacles:
            i = random.randint(0, grid_size)
            j = random.randint(0, grid_size)

            if cells[i][j].getPassable() and not cells[i][j].getEndstate():
                location = Location(i, j)
                cell = Cell(location=Location(i, j), width=width_of_cell, 
                height=hieght_of_cell, percept=GOAL_CELL, 
                direction=Constants.FACING_WEST)

                cell.setEndstate(True)
                this.add(cell, j, i) #check on what this is 
                cells[i][j] = cell
                cells[i][j].setPassable(True)
                goals[count] = cells[i][j]
                count+=1

    def getPercepts():
        for i in range(0, grid_size):
            for j in range(0, grid_size):
                perceptsOfCells[i][j] = Percept()
        
        for i in range(0, grid_size):
            for j in range(0, grid_size):
                try:
                    perceptsOfCells[i][j].setNorthPercept(cells[i - 1][j].getPercept())
                except IndexError:
                    perceptsOfCells[i][j].setNorthPercept(BORDER)
                
                try:
                    perceptsOfCells[i][j].setWestPercept(cells[i][j - 1].getPercept())
                except IndexError:
                    perceptsOfCells[i][j].setWestPercept(BORDER)
                
                try:
                    perceptsOfCells[i][j].setEastPercept(cells[i][j + 1].getPercept())
                except IndexError:
                    perceptsOfCells[i][j].setEastPercept(BORDER)
                
                try:
                    perceptsOfCells[i][j].setSouthPercept(cells[i + 1][j].getPercept())
                except IndexError:
                    perceptsOfCells[i][j].setSouthPercept(BORDER)
        return perceptsOfCells





if __name__=="__main__":
    enviroment = enviroment(10)
    enviroment.create_grid()