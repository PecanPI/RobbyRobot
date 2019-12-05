import robby
import cleaningSession


generations = 1000
cleaning_sessions = 100
population_size = 2
population = []

for i in range(generations):
    if i == 0:  # intial population
        for j in range(population_size):
            population.append(robby.Robby())

for j in population:
    for k in range(cleaning_sessions):
        print(f'run %s Fitness: %s' % (k, cleaningSession.cleaning(j)))


