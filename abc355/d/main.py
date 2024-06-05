import sys
sys.setrecursionlimit(300000)

N = int(sys.stdin.readline().rstrip())
lrs = [[] for _ in range(N)]
for i in range(N):
    l, r = list(map(int, sys.stdin.readline().rstrip().split()))
    lrs[i] = [l, r]
lrs.sort()

d = [0] * (10**9+2)
res = 0
for l, r in lrs:
    for i in range(l+1):
        res += d[i]
    d[l] += 1
    d[r+1] -= 1
print(res)
