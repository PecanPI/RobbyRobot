import robby
import numpy as np


generations = 1000
cleaning_sessions = 100
population_size = 200
population = []

for i in range(generations):
    if i == 0:  # intial population
        for j in range(population_size):
            population.append(robby.Robby())

    for j in population:

        print(j.gene)

