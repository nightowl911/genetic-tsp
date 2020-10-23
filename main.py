import random
from tqdm import tqdm
from Path import Path, n, start
import math

psize = 500
generations = 1
limit = 500
bestScore = 10000000000
# pm = 0

population = []

for i in range(psize):
    population.append(Path())

bestPath = list(range(1, n))
pbar = tqdm(total=limit)

for i in population:
    if i.score < bestScore:
        bestScore = i.fitness
        bestPath = i.path
        s = "Generation: " + str(generations) + " Score: " + str(bestScore)


# pbar.update(1)

while generations <= limit:

    parents = population[:]
    matingPool = []
    parents.sort(key=lambda x: (x.score)) # [142 142 140 109 109 109]
    totalFitness = sum(x.score for x in parents)
    cumilative = 0
    cumilativeList = []
    for i in parents:
        cumilative += (i.score)
        cumilativeList.append(cumilative / totalFitness) # [ 0.5 0.7 0.9 1]

    population = []

    while len(population) < (math.ceil(0.75*psize)):
        x = random.random()
        y = random.random()
        i = 0
        done = 0
        while i < len(cumilativeList) and done == 0:
            if x < cumilativeList[i]:
                done = 1
            else:
                i += 1
        j = 0
        done = 0
        while j < len(cumilativeList) and done == 0:
            if y < cumilativeList[j]:
                done = 1
            else:
                j += 1

        if i != j:
            child1 = parents[i].crossover2(parents[j])
            child2 = parents[j].crossover2(parents[i])
            child1.mutate()
            child2.mutate()


            population.append(child1)
            population.append(child2)
    # print("Population Size: ", len(population))
    population = population + parents[math.ceil(0.75*psize):] #[75:100]
    population.sort(key=lambda x: (x.score))
    population = population[-psize:]

    for i in population:
        if i.fitness < bestScore:
            bestScore = i.fitness
            bestPath = i.path
            s = "Generation: " + str(generations) + " Score: " + str(bestScore) + " Population: " + str(psize)
            pbar.set_description(s)

    pbar.update(1)
    generations += 1

print()
print("BestScore: ", bestScore)
route = str(start) + ' -> ' + ' -> '.join(str(x) for x in bestPath) + ' -> ' + str(start)
print("BestPath: ", route)
