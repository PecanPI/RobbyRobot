import robby
import game
import breeding
import cleaningSession
import threading

generations = 1001
cleaning_sessions = 100
population_size = 10
population = []

for i in range(generations):
    print(f'Generation %s:' % i)
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
            #print(f'run %s Fitness: %s' % (k, f))
        fitness = fitness/cleaning_sessions
        population[j].append(fitness)

    population.sort(key=lambda x: x[1], reverse=True)

    if i % 200 == 0:
        thread = threading.Thread(target = game.gameloop, args=(population[0][0],), daemon=True)
        #thread.start()

        #game.gameloop(population[0][0])
        thread.start()

    #thread.join()
    print(population[0][1])
    breeding.breed(population)

