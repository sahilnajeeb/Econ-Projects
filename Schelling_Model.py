import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
from random import uniform

#Define object:

class Agent:
    def __init__(self, location, color):
        self.location = self.draw_location()
        self.color = color
        
    def draw_location(self):
        location = (uniform(0, 1), uniform(0, 1))
        return location
    def distance(self,other):
        a = (self.location[0] - other.location[0])**2
        b = (self.location[1] - other.location[1])**2
        return sqrt(a + b)
    def happy(self,agents, neighborhood_size=10, unhappy_criteria=5):
        
        for agent in agents:
            if agent==self:
                pass
            else:
                distance = self.distance(agent)
                
                sorted_distances = sorted(agents, key=lambda agent: self.distance(agent))
                unhappy_count = 0
                for agent in sorted_distances[:neighborhood_size]:
                    if agent.color != self.color:
                        unhappy_count += 1
                    else:
                        pass
                return unhappy_count < unhappy_criteria

#Graphing function:

def plot_distribution(agents, cycle_num):
    "Plot the distribution of agents after cycle_num rounds of the loop."
    x_values_blue, y_values_blue = [], []
    x_values_red, y_values_red = [], []
    x_values_green, y_values_green = [],[]
    x_values_yellow, y_values_yellow = [],[]
    # == Obtain locations of each type == #
    for agent in agents:
        x, y = agent.location
        if agent.color == 'blue':
            x_values_blue.append(x)
            y_values_blue.append(y)
        elif agent.color == 'red':
            x_values_red.append(x)
            y_values_red.append(y)
        elif agent.color == 'yellow':
            x_values_yellow.append(x)
            y_values_yellow.append(y)
        else:
            x_values_green.append(x)
            y_values_green.append(y)           
    fig, ax = plt.subplots()
    plot_args = {'markersize': 8, 'alpha': 0.8}
    ax.set_facecolor('azure')
    ax.plot(x_values_blue, y_values_blue,
        'o', markerfacecolor='blue', **plot_args)
    ax.plot(x_values_red, y_values_red,
        'o', markerfacecolor='red', **plot_args)
    ax.plot(x_values_green, y_values_green,
        'o', markerfacecolor='green', **plot_args)
    ax.plot(x_values_yellow, y_values_yellow,
        'o', markerfacecolor='yellow', **plot_args)
    
    ax.set_title(f'Iteration {cycle_num}')
    plt.show()

#SCHELLING ALGORITHM 1: Goes through each cycle then moves unhappy agents all at once

def run_simulation1(max_iterations=1000, num_of_blue=200, num_of_red=200, num_of_green=200, num_of_yellow=200):
    #Create agents:

    blue_numbers = [np.random.uniform(0,1) for i in range(num_of_blue)]
    red_numbers = [np.random.uniform(0,1) for i in range(num_of_red)]
    green_numbers = [np.random.uniform(0,1) for i in range(num_of_green)]
    yellow_numbers = [np.random.uniform(0,1) for i in range(num_of_yellow)]
    blue_agents = [Agent(blue_numbers[i],'blue') for i in range(num_of_blue)]
    red_agents = [Agent(red_numbers[i],'red') for i in range(num_of_red)]
    green_agents = [Agent(green_numbers[i],'green') for i in range(num_of_green)]
    yellow_agents = [Agent(yellow_numbers[i],'yellow') for i in range(num_of_yellow)]
    agents = blue_agents + red_agents + green_agents+yellow_agents
    iterations = 0
    plot_distribution(agents,iterations)

    #Check if happy

    checker = True
    while checker:
        count = 0
        for agent in agents:
            flag = agent.happy(agents)
            if flag:
                count += 1
            else:
                agent.location = agent.draw_location()
        if count < len(agents):
            iterations += 1
            plot_distribution(agents,iterations)
        else:
            checker = False
            iterations += 1
        if iterations < max_iterations:
            pass
        else:
            break

    plot_distribution(agents,iterations)
    if iterations < max_iterations:
        print(f"Converged after {iterations} iterations.")
    else:
        print("Max iterations reached.")    

#SCHELLING ALGORITHM 2: Goes through and moves each agent individually, then goes back to beginning of list

def run_simulation2(max_iterations=1000, num_of_blue=100, num_of_red=100):
    #Create agents:

    blue_numbers = [np.random.uniform(0,1) for i in range(num_of_blue)]
    red_numbers = [np.random.uniform(0,1) for i in range(num_of_red)]
    blue_agents = [Agent(blue_numbers[i],'blue') for i in range(num_of_blue)]
    red_agents = [Agent(red_numbers[i],'red') for i in range(num_of_red)]
    agents = blue_agents + red_agents
    iterations = 0
    plot_distribution(agents,iterations)
    
    #Check if happy:

    checker = True
    while checker:
        count = 0
        for agent in agents:
            flag = agent.happy(agents)
            if flag:
                count += 1
            else:
                agent.location = agent.draw_location()
                break
        if count < len(agents):
            iterations += 1
            plot_distribution(agents,iterations)
        else:
            checker = False
            iterations += 1
        if iterations < max_iterations:
            pass
        else:
            break
            
    plot_distribution(agents,iterations)
    if iterations < max_iterations:
        print(f"Converged after {iterations} iterations.")
    else:
        print("Max iterations reached.")    

