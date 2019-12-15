import robby
import random
import numpy.random as npr

mutate_rate = 50

# breeds a new population
def breed(population):
    newpop = []
    for i in range(int(len(population)/2)):
        rand = random.randint(0, int(len(population)/2 - 1 ))
        child1 = [robby.Robby()]
        child2 = [robby.Robby()]
        #gene1, gene2 = singlePointCrossover(population[i][0].gene, population[rand][0].gene)
        gene1, gene2 = singlePointCrossover(weightedChoice(population[0:100]).gene, weightedChoice(population[0:100]).gene)
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
        if (random.randint(0, 1000)) <= mutate_rate:
            newrob[i] = str(random.randint(0, 6))
    rob.set_gene("".join(newrob))
    return rob

#wighted choice higher fitness has a higher probability to breed
def weightedChoice(population):
    weight_total = sum((rob[2] for rob in population))
    selection_prob = [(rob[2])/weight_total for rob in population]
    current = 0
    choice = population[npr.choice(len(population), p=selection_prob)]

    return choice[0]

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
            child2 += parent2[i]
        else:
            child1 += parent2[i]
            child2 += parent1[i]
    return child1, child2


def twoPointCrossover(p1, p2):
    parent1 = list(p1)
    parent2 = list(p2)
    child1 = ""
    child2 = ""

