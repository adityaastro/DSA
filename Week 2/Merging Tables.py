import sys


class DisjSet:
    def __init__(self, l):
        self.parents = [-1] * len(l)
        self.rank = [Height for Height in l]
        self.max = max(self.rank)

    def find(self, element):
        update = []
        while self.parents[element] != -1:
            update.append(element)
            element = self.parents[element]

        for i in update:
            self.parents[i] = element
            
        return element

    def union(self, i, j):
        I = self.find(i)
        J = self.find(j)
        if I == J:
            return
        if self.rank[I] > self.rank[J]:
            self.parents[J] = I
            self.rank[I] += self.rank[J]
        else:
            self.parents[I] = J
            self.rank[J] += self.rank[I]

        m = max(self.rank[I], self.rank[J])
        if m > self.max:
            self.max = m

    def __repr__(self):
        return "DisjSet({})".format(self.parents)


n, m = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))
D = DisjSet(l)
Q = []
for _ in range(m):
    Q.append(tuple(map(int, sys.stdin.readline().split())))

for i, j in Q:
    D.union(i - 1, j - 1)
    print(D.max)
