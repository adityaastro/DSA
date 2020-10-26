from sys import stdin as s


class HashTable:
    def __init__(self, m):
        self.m = m
        self.arr = [None] * self.m
        self.p = 1000000007
        self.n = 0

    def hash(self, data):
        x = 263
        h = 0
        if str(data).isdigit():
            return data
        for i in range(len(data)):
            h += ord(data[i]) * (x**i)
        return ((h % self.p) % self.m)

    def remove(self, key):
        h = self.hash(key)
        if self.arr[h]:
            for i in range(len(self.arr[h])):
                if self.arr[h][i] == key:
                    del self.arr[h][i]
                    return

    def __getitem__(self, key):
        h = self.hash(key)
        if not self.arr[h]:
            return ' '
        return ' '.join(self.arr[h][::-1])

    def find(self, key):
        h = self.hash(key)
        if not self.arr[h]:
            return 'no'
        else:
            for i in self.arr[h]:
                if i == key:
                    return 'yes'
            return 'no'

    def add(self, key):
        h = self.hash(key)
        if self.arr[h]:
            for i in self.arr[h]:
                if i == key:
                    return
            self.arr[h].append(key)
        else:
            self.arr[h] = [key]

    def __repr__(self):
        return "HashTable({})".format(self.arr)

m = int(s.readline())
H = HashTable(m)
Ans = []
for _ in range(int(s.readline())):
    q = s.readline().split()
    q[1] = str(q[1])
    if q[0] == 'add':
        H.add(q[1])
        
    elif q[0] == 'check':
        Ans.append(H[int(q[1])])

    elif q[0] == 'find':
        Ans.append(H.find(q[1]))

    elif q[0] == 'del':
        H.remove(q[1])

print(*Ans, sep='\n')
