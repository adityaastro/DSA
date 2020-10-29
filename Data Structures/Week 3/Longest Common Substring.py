import sys
from random import randint as r

sys.setrecursionlimit(10**8)


def PH(S, p, x):
    lS = len(S)
    H1 = [0] * (lS[0] + 1)
    H2 = [0] * (lS[1] + 1)
    l = max(len(S[0]), len(S[1]))
    for i in range(l):
        if i < len(S[0]):
            H1[i + 1] = (x * H1[i] + ord(S[0][i])) % p
        if i < len(S[1]):
            H2[i + 1] = (x * H2[i] + ord(S[1][i])) % p
    return H1, H2


def compare(S, x, p, lb=0, ub=(min(len(S[0]), len(S[1])))):
    global H1, H2
    flag = True
    l = (lb + ub) // 2
    l1, l2 = len(S[0]), len(S[1])
    L = max(l1, l2)
    y = pow(x, l, p)
    h1 = {(H1[i + l] - y * H1[i]) % p: i for i in range(l1 - l)}
    for i in range(l2 - l):
        h2 = (H2[i + l] - y * H2[i]) % p
        if h2 in h1:
            flag = False
            return compare(S, x, p, l, ub)
            break
    if flag:
        compare(S, x, p, lb, l)

p = 1000000007
x = r(1, p - 1)
H1, H2 = PH(S, p, x)
q = tuple(map(str, input().split()))
Ans = [compare(i, x, p) for i in q]
print(*Ans, sep='\n')
