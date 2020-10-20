import heapq
import sys

n, m = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))
Q = []

for i in range(n):
    if i >= m:
        break
    heapq.heappush(Q, (l[i], i))
    print(i, 0)

for i in range(n, m):
    Min = heapq.heappop(Q)
    heapq.heappush(Q, (l[i] + Min[0], Min[1]))
    print(Min[1], Min[0])
