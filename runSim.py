import robby
import game
import breeding
import cleaningSession
import threading
import matplotlib.pyplot as plt

generations = 1001
cleaning_sessions = 100
population_size = 200
population = []
average_fitness = []
max_fitness = []


for i in range(generations):
    print(f'Generation %s:' % i)
    if i == 0:  # intial population
        for j in range(population_size):
            new = [robby.Robby()]
            population.append(new)
    else:
        population = breeding.breed(population)
        #print(population)

    for j in range(len(population)):
        fitness = 0
        for k in range(cleaning_sessions):
            f = cleaningSession.cleaning(population[j][0])
            fitness = f + fitness
            #print(f'run %s Fitness: %s' % (k, f))
        fitness = fitness/cleaning_sessions
        population[j].append(fitness)

    population.sort(key=lambda x: x[1], reverse=True)
    max_fitness.append(population[0][1])
    sum = 0
    for j in population:
        sum += j[1]
    average_fitness.append(sum/len(population))

    if i % 200 == 0:
        thread = threading.Thread(target = game.gameloop, args=(population[0][0],))
        thread.start()

    #thread.join()
    #print(population[0][1])
    print('Highest Fitness: ', max_fitness[i])
    print('Average Fitness: ', average_fitness[i])
    #breeding.breed(population)

