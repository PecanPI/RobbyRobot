import robby
import cleaningSession


generations = 1000
cleaning_sessions = 100
population_size = 2
population = [[], []]


for i in range(generations):
    if i == 0:  # intial population
        for j in range(population_size):
            population[j].append(robby.Robby())


for i in range(len(population)):
    fitness = 0
    for k in range(cleaning_sessions):
        f = cleaningSession.cleaning(population[i][0])
        fitness = f + fitness
        #print(f'run %s Fitness: %s' % (k, f))
    fitness = fitness/cleaning_sessions
    population[i].append(fitness)


#easier read format
for p in population:
    print(p)

