import heapq
import sys

Swaps = []
def p(i):
    return (i - 1) // 2


def l(i):
    return 2 * i + 1


def r(i):
    return 2 * i + 2


def SiftDown(i, heap):
    index = i
    L = l(i)
    R = r(i)
    if L < len(heap) and heap[L] < heap[index]:
        index = L
    if R < len(heap) and heap[R] < heap[index]:
        index = R
    if i != index:
        heap[i], heap[index] = heap[index], heap[i]
        Swaps.append((i, index))
        SiftDown(index, heap)



N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
i = N//2
while i >= 0:
    SiftDown(i, arr)
    i -= 1

print(len(Swaps))
for tup in Swaps:
    print(*tup)
