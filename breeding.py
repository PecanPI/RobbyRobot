import robby
import random

mutate_rate = 0.02

# breeds a new population
def breed(population):
    newpop = []
    for i in range(int(len(population)/2)):
        rand = random.randrange(int(len(population)/2))
        child1 = [robby.Robby()]
        child2 = [robby.Robby()]
        gene1, gene2 = singlePointCrossover(population[i][0].gene, population[rand][0].gene)
        child1[0].set_gene(gene1)
        child2[0].set_gene(gene2)
        child1[0] = mutate(child1[0])
        child2[0] = mutate(child2[0])
        newpop.append(child1)
        newpop.append(child2)

    return newpop

# mutates random genes
def mutate(rob):
    newrob = list(rob.gene)
    for i in range(len(newrob)):
        if (random.randrange(1000) / 1000) < mutate_rate:
            newrob[i] = str(random.randint(0, 6))

    rob.set_gene("".join(newrob))
    return rob


# takes two parents and performs a single point crossover
# returns two children
def singlePointCrossover(p1, p2):
    parent1 = list(p1)
    parent2 = list(p2)
    child1 = ""
    child2 = ""
    crossover_point = random.randint(0, len(p1))
    for i in range(len(p1)):
        if i <= crossover_point:
            child1 += parent1[i]
        else:
            child1 += parent2[i]

    for i in range(len(p1)):
        if i >= crossover_point:
            child2 += parent1[i]
        else:
            child2 += parent2[i]
    return child1, child2


def twoPointCrossover(p1, p2):
    parent1 = list(p1)
    parent2 = list(p2)
    child1 = ""
    child2 = ""

