import robby
import random

mutate_rate = 0.005


def mutate(rob):
    newrob = list(rob)
    for i in range(len(newrob)):
        if (random.randrange(1000) / 1000) < mutate_rate:
            newrob[i] = str(random.randint(0, 6))

    rob = "".join(newrob)
    return rob


def singlePointCrossover(p1, p2):
    parent1 = list(p1)
    parent2 = list(p2)
    child = ""
    crossover_point = random.randint(0, len(p1))
    for i in range(len(p1)):
        if i <= crossover_point:
            child += parent1[i]
        else:
            child += parent2[i]

    return child