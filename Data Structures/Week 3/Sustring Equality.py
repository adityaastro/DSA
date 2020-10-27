from random import randint as r

def PH(S, p1, p2, x):
    lS = len(S)
    H1 = [0] * (lS + 1)
    H2 = [0] * (lS + 1)
    for i in range(lS):
        H1[i + 1] = (x * H1[i] + ord(S[i])) % p1
        H2[i + 1] = (x * H2[i] + ord(S[i])) % p2

    return H1, H2


def compare(S, q, x, p1, p2):
    global H1, H2
    y1 = pow(x, q[2], p1)
    y2 = pow(x, q[2], p2)

    h11 = (H1[q[0] + q[2]] - y1 * H1[q[0]]) % p1
    h12 = (H2[q[0] + q[2]] - y2 * H2[q[0]]) % p2
    h21 = (H1[q[1] + q[2]] - y1 * H1[q[1]]) % p1
    h22 = (H2[q[1] + q[2]] - y2 * H2[q[1]]) % p2
    if h11 == h21 and h12 == h22:
        return 'Yes'
    return 'No'


S = input()
p1 = 1000000007
p2 = 1000000009
x = r(1, p1 - 1)
H1, H2 = PH(S, p1, p2, x)
Q = int(input())
q = [tuple(map(int, input().split())) for _ in range(Q)]
Ans = [compare(S, i, x, p1, p2) for i in q]
# print(H1, H2)
print(*Ans, sep='\n')
