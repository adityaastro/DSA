def hash(S, p, x):
    h = 0
    for i in reversed(S):
        h = (h * x + ord(i)) % p
    return h

# def hash(S, p, x):
#     temp=0
#     a=1
#     for i in S:
#         temp=(temp+(ord(i)*a))%p
#         a*=x
#     return temp


def PH(S, P, p, x):
    lP, lS = len(P), len(S)
    s = hash(S[-lP:], p, x)
    i = lS - lP - 1
    H = [0] * (i + 2)
    H[lS - lP] = s
    y = 1
    for _ in range(1, lP+1):
        y = (y * x) % p
    while i >= 0:
        H[i] = (x * H[i + 1] + ord(S[i]) - y * ord(S[i + lP])) % p
        i -= 1
    return H


x = 2
p = 11
P = input()
S = input()
lP, lS = len(P), len(S)
h = hash(P, p, x)
H = PH(S, P, p, x)
Ans = [str(i) for i in range(len(H)) if H[i] == h]
print(H)
print(' '.join(Ans))
