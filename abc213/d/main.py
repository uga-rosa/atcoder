import sys

sys.setrecursionlimit(300000)


N = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = list(map(int, sys.stdin.readline().rstrip().split()))
    graph[a].append(b)
    graph[b].append(a)

for i in range(N + 1):
    graph[i].sort()

ans = []


# graphは木なのでこれでいい
def dfs(cur, pre):
    ans.append(cur)
    for nxt in graph[cur]:
        if nxt != pre:
            dfs(nxt, cur)
            ans.append(cur)


dfs(1, -1)
print(*ans)
