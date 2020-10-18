import random
from tqdm import tqdm
from Path import Path, n, start, graph

psize = 500

population = []

for i in range(psize):
    population.append(Path())

generations = 1
ngenerations = 1000
bestScore = 10000000000
bestPath = list(range(1, n))
pbar = tqdm(total=ngenerations)
# pbar.update(1)

for i in population:
    if i.getFitness() < bestScore:
        bestScore = i.fitness
        bestPath = i.path
        # print("---------------Updated---------------")
        # print("Generation: ",generations, "Score:", bestScore);
        s = "Generation: " + str(generations) + " Score: " + str(bestScore)

while generations <= ngenerations:

    parents = population[:]
    matingPool = []

    max_fitness = max(parents, key=lambda x: x.fitness)
    min_fitness = min(parents, key=lambda x: x.fitness)
    th = (max_fitness.fitness + min_fitness.fitness) // 2
    th = (2/((1/max_fitness.fitness) + (1/min_fitness.fitness)))
    # print(min_fitness.fitness, max_fitness.fitness, th)
    parents.sort(key=lambda x: (x.fitness))
    # totalFitness = sum((1 / x.fitness) for x in parents)
    # cumilative = 0
    # cumilativeList = []
    # for i in parents:
    #     cumilative += (1 / i.fitness)
    #     cumilativeList.append(cumilative / totalFitness)
    # cumilativeList = cumilativeList
    # print(cumilativeList)

    # print(parents[0].fitness)
    #
    unfitList = []
    for i in range(len(parents)):
        if parents[i].fitness <= th:
            matingPool.append(parents[i])

    # matingPool = parents[:]
    # print("Mating Pool Size: ", len(matingPool))

    population = []

    while len(population) <  (psize):
        if random.random() < 0.7:
            x = random.choice(matingPool)
            y = random.choice(matingPool)
        else:
            x = random.choice(parents)
            y = random.choice(parents)
        # print(x.path)
        # print(y.path)
        if y != x:
            # if random.random() < 0.5:
            #     child = matingPool[x].crossover2(matingPool[y])
            # else:
            child = x.crossover2(y)
            child2 = y.crossover2(x)
            child.mutate()
            child2.mutate()

            population.append(child)
            population.append(child2)
    # print("Population Size: ", len(population))

    for i in population:
        if i.getFitness() < bestScore:
            bestScore = i.fitness
            bestPath = i.path
            # print("---------------Updated---------------")
            # print("Generation: ",generations, "Score:", bestScore);
            s = "Generation: " + str(generations) + " Score: " + str(bestScore)
            pbar.set_description(s)

    # population.sort(key=lambda x: (x.fitness))
    # population = population[0:psize]
    pbar.update(1)
    # pbar.set_description("Generation: ",generations, "Score:", bestScore)
    generations += 1

print()
print("BestScore: ", bestScore)
route = str(start) + ' -> ' + ' -> '.join(str(x) for x in bestPath) + ' -> ' + str(start)
print("BestPath: ", route)

