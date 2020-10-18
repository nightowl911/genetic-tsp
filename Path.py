import random
graph = [[0,633,257,91,412,150,80,134,259,505,353,324,70,211,268,246,121],
    [633,0,390,661,227,488,572,530,555,289,282,638,567,466,420,745,518],
    [257,390,0,228,169,112,196,154,372,262,110,437,191,74,53,472,142],
    [91,661,228,0,383,120,77,105,175,476,324,240,27,182,239,237,84],
    [412,227,169,383,0,267,351,309,338,196,61,421,346,243,199,528,297],
    [150,488,112,120,267,0,63,34,264,360,208,329,83,105,123,364,35],
    [80,572,196,77,351,63,0,29,232,444,292,297,47,150,207,332,29],
    [134,530,154,105,309,34,29,0,249,402,250,314,68,108,165,349,36],
    [259,555,372,175,338,264,232,249,0,495,352,95,189,326,383,202,236],
    [505,289,262,476,196,360,444,402,495,0,154,578,439,336,240,685,390],
    [353,282,110,324,61,208,292,250,352,154,0,435,287,184,140,542,238],
    [324,638,437,240,421,329,297,314,95,578,435,0,254,391,448,157,301],
    [70,567,191,27,346,83,47,68,189,439,287,254,0,145,202,289,55],
    [211,466,74,182,243,105,150,108,326,336,184,391,145,0,57,426,96],
    [268,420,53,239,199,123,207,165,383,240,140,448,202,57,0,483,153],
    [246,745,472,237,528,364,332,349,202,685,542,157,289,426,483,0,336],
    [121,518,142,84,297,35,29,36,236,390,238,301,55,96,153,336,0]]

n = len(graph)
print("Nodes:", n)
start = 0

class Path:
    def __init__(self):
        self.path = list(range(0,n)) # 0th node path to 0th
        self.path.remove(start)
        random.shuffle(self.path)
        self.fitness = self.getFitness()
        # print(self.path)

    def getFitness(self):
        pre = start
        score = 0
        for i in range(len(self.path)):
            score += graph[pre][self.path[i]]
            pre = self.path[i]
        score += graph[self.path[-1]][start]
        self.fitness = score
        # print("Path: ",self.path)
        # print("Score: ",score)
        return score

    def crossover1(self, partner):
        h = (n - 1) // 2
        p = list.copy(partner.path)
        try:
            for i in range(h, n - 1):
                p.remove(self.path[i])
        except Exception as e:
            print("h: ", h, "n: ", n)
            # print(h, n-1)
            print(e)
            exit()
        child = Path()
        child.path = p
        for i in range(h, n - 1):
            child.path.append(self.path[i])

        child.fitness = child.getFitness()
        return child

    def crossover2(self, partner):
        h = (n-1)//2
        a = random.choice(range(1,h))
        b = random.choice(range(h,n-1))
        # p = self.path[0:a] + partner.path[a:b] + self.path[b:(n-1)]
        p = []
        # print(self.path)
        # print(partner.path)
        # print(a,b)
        tmp = self.path[a:b]

        i = 0
        j = 0
        while i < a:
            if partner.path[j] not in tmp:
                p += [partner.path[j]]
                i += 1
                j += 1
            else:
                j += 1

        p += tmp
        i = b
        while i < n-1:
            if partner.path[j] not in tmp:
                p += [partner.path[j]]
                i += 1
                j += 1
            else:
                j += 1

        # print(p)

        child = Path()
        child.path = p

        child.fitness = child.getFitness()
        return child

    def mutate(self):
        if random.random() < 0.05:
            x = random.choice(range(0,n-1))
            y = random.choice(range(0,n-1))

            t = self.path[x]
            self.path[x] = self.path[y]
            self.path[y] = t
            self.fitness = self.getFitness()
