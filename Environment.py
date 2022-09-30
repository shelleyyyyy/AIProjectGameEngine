from Location import Location
from Cell import Cell

class enviroment:
    width, height = (10, 10)

    def __init__(self, num_of_agents = 0, num_of_goals = 0, num_of_non_passable = 0):
        self.num_of_agents = num_of_agents
        self.num_of_goals = num_of_goals
        self.num_of_non_passable = num_of_non_passable

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
                #cell() create a cell. need cell class


if __name__=="__main__":
    enviroment = enviroment(10)
    enviroment.create_grid()