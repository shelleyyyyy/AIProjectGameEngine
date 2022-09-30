class enviroment:
    width, height = (10, 10)
    num_of_agents = 0
    num_of_goals = 0
    num_of_non_passable = 0

    def __init__(self, num_of_agents = 0, num_of_goals = 0, num_of_non_passable = 0):
        self.num_of_agents = num_of_agents
        self.num_of_goals = num_of_goals
        self.num_of_non_passable = num_of_non_passable

    def create_grid(self):
        env = [[0] * self.width] * self.height
        print(env)
        print(self.num_of_agents)
    



if __name__=="__main__":
    enviroment = enviroment(10)
    enviroment.create_grid()