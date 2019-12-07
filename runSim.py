import robby
import game
import breeding
import cleaningSession


generations = 1000
cleaning_sessions = 100
population_size = 5
population = []


for i in range(generations):
    if i == 0:  # intial population
        for j in range(population_size):
            new = [robby.Robby()]
            population.append(new)


for i in range(len(population)):
    fitness = 0
    for k in range(cleaning_sessions):
        f = cleaningSession.cleaning(population[i][0])
        fitness = f + fitness
        #print(f'run %s Fitness: %s' % (k, f))
    fitness = fitness/cleaning_sessions
    population[i].append(fitness)


population.sort(key=lambda x: x[1], reverse=True)
print()
for p in population:
    print(p)

#game.gameloop(population[0][0])

population[0][0].set_gene(breeding.mutate(population[0][0].gene))
print(population[0][0])

print(breeding.singlePointCrossover(population[0][0].gene, population[1][0].gene))
