import sys

sys.setrecursionlimit(300000)


S, K = list(sys.stdin.readline().rstrip().split())
K = int(K) - 1
l = len(S)

res = []
t = []


def find(fl):
    global t
    if fl == 0:
        res.append("".join(t))
    else:
        for i in range(l):
            if fl & (1 << i):
                t.append(S[i])
                find(fl ^ (1 << i))
                t.pop()


find((1 << l) - 1)
res = list(set(res))
res.sort()
print(res[K])
