import sys
sys.setrecursionlimit(10**6)

N = int(input())
g = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(lambda x: int(x)-1, input().split())
    g[a].append(b)
    g[b].append(a)

# 自身の下にあるノード (自身を含む) の数
count = [0] * N
def dfs(crr, pre):
    s = 1
    for nxt in g[crr]:
        if nxt != pre:
            s += dfs(nxt, crr)
    count[crr] = s
    return s
dfs(0, -1)

ans = 0
for i in range(N):
    ans += count[i] * (N - count[i])
print(ans)
