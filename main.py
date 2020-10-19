import random
from tqdm import tqdm
from Path import Path,n,start
import math

psize = 300
ipsize = psize

population = []

for i in range(psize):
    population.append(Path())

pr = 1

generations = 1
limit = 500
bestScore = 10000000000
bestPath = list(range(1,n))
pbar = tqdm(total=limit)
# pbar.update(1)
while generations <= limit:

    parents = population
    matingPool = []

    parents.sort(key=lambda x:(x.score))
    totalFitness = sum(x.score for x in parents)
    # print(totalFitness)
    cumilative = 0
    cumilativeList = []
    for i in parents:
        cumilative += (i.score)
        cumilativeList.append(cumilative/totalFitness)
    # cumilativeList = cumilativeList
    # for i in parents:
    #     print(i.fitness, end=" ")
    # print()
    # for i in parents:
    #     print(1/i.fitness, end=" ")
    # print()
    # print(cumilativeList)
    
    # print(parents[0].fitness)
    #
    # for i in range(len(parents)):
    #     if parents[i].fitness <= th:
    #         matingPool.append(parents[i])

    # matingPool = parents[:]
    # print("Mating Pool Size: ", len(matingPool))

    population = []

    while len(population) < (3*(psize)):
        x = random.random()
        y = random.random()
        i = 0
        done = 0
        while i < len(cumilativeList) and done == 0:
            if x < cumilativeList[i]:
                done = 1
            else:
                i += 1
        # print("Random: ", x, "Choosing: ", i, parents[i].fitness)
        j = 0
        done = 0
        while j < len(cumilativeList) and done == 0:
            if y < cumilativeList[j]:
                done = 1
            else:
                j += 1
        # print("Random: ", y, "Choosing: ", j, parents[j].fitness)
        # print(x.path)
        # print(y.path)
        # if i != j:
        #     if random.random() < 0.5:
        #         child = matingPool[x].crossover2(matingPool[y])
        #     else:
        #         child = matingPool[x].crossover2(matingPool[y])
        #     child.mutate()
        #
        #     population.append(child)
        if i != j:

            child1 = parents[i].crossover2(parents[j])
            child2 = parents[j].crossover2(parents[i])
            child1.mutate()
            child2.mutate()
            if pr == 1:
                print(parents[i].path, sum(parents[i].path))
                print(parents[j].path, sum(parents[j].path))
                print(child1.path, sum(child1.path))
                pr = 0

            population.append(child1)
            population.append(child2)
    # print("Population Size: ", len(population))
    # population = population + parents[3*(psize//4):]
    population.sort(key=lambda x:(x.score))
    # psize = math.ceil(psize+1.001)
    # print(psize, bestScore)
    # print(psize)
    # if pr == 1:
    #     for i in population:
    #         print(i.score, end=" ")
    #     print()

    population = population[-psize:]
    # print(psize, bestScore, len(population))

    # if pr == 1:
    #     for i in population:
    #         print(i.score, end=" ")
    #     print()
    #     pr = 2



    for i in population:
        if i.fitness < bestScore:
            bestScore = i.fitness
            bestPath = i.path
            # print("---------------Updated---------------")
            # print("Generation: ",generations, "Score:", bestScore);
            s = "Generation: " + str(generations) + " Score: " + str(bestScore) #+ " Population: " + str(ipsize) + "->" + str(len(population))
            pbar.set_description(s)

    pbar.update(1)
    # pbar.set_description("Generation: ",generations, "Score:", bestScore)
    generations += 1

print()
print("BestScore: ", bestScore)
print("Initial Population: ", ipsize)
print("Final Population: ", psize)
route = str(start) + ' -> ' + ' -> '.join(str(x) for x in bestPath) + ' -> ' + str(start)
print("BestPath: ", route)

