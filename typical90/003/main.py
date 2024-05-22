import sys
import numpy as np

sys.setrecursionlimit(300000)


# 制約から元々が木と分かる
# 問題文をいいかえると、最も遠いノード間の距離はいくらか？
N = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = list(map(int, sys.stdin.readline().rstrip().split()))
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)


R = [-1] * N


def dfs(crr, pre, rank):
    R[crr] = rank
    for nxt in graph[crr]:
        if nxt != pre:
            dfs(nxt, crr, rank + 1)


dfs(0, -1, 1)
i = np.argmax(R)
dfs(i, -1, 1)
print(max(R))
