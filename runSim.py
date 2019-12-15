import robby
import game
import breeding
import cleaningSession
import threading
import multiprocessing

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

generations = 1001
cleaning_sessions = 100
population_size = 200
population = []
average_fitness = []
max_fitness = []
generationArray = []

plt.axis([0, 1000, -100, 500])
plt.xlabel('Generation')
plt.ylabel('Fitness')

for i in range(generations):
    print(f'Generation %s:' % i)
    generationArray.append(i)
    if i == 0:  # intial population
        for j in range(population_size):
            new = [robby.Robby()]
            population.append(new)
    else:
        population = breeding.breed(population)

    for j in range(len(population)):
        fitness = 0
        for k in range(cleaning_sessions):
            f = cleaningSession.cleaning(population[j][0])
            fitness = f + fitness
        fitness = fitness / cleaning_sessions
        population[j].append(fitness)
        weight = (fitness - (-1000)) / (500 - (-1000))
        population[j].append(weight)

    population.sort(key=lambda x: x[1], reverse=True)
    max_fitness.append(population[0][1])
    sum = 0
    for j in population:
        sum += j[1]
    average_fitness.append(sum / len(population))

    if i % 50 == 0:
        thread = threading.Thread(target=game.gameloop, args=(population[0][0],))
        thread.start()
    print('Highest Fitness: ', max_fitness[i])
    print('Average Fitness: ', average_fitness[i])
    plt.scatter(i, max_fitness[i], s=1, color='b')
    plt.pause(0.05)

plt.show()