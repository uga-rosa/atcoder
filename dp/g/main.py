import sys

sys.setrecursionlimit(300000)


N, M = list(map(int, sys.stdin.readline().rstrip().split()))
graph = [[] for _ in range(N)]
# 入次数
# indegree = [0] * N
for i in range(M):
    x, y = list(map(int, sys.stdin.readline().rstrip().split()))
    graph[x - 1].append(y - 1)
    # indegree[y - 1] += 1

# メモ化再帰
# dp[i] := 頂点iからの最長経路の長さ
dp = [-1] * N


def rec(n):
    if dp[n] != -1:
        return dp[n]
    res = 0
    for m in graph[n]:
        res = max(res, rec(m) + 1)
    dp[n] = res
    return res


for i in range(N):
    rec(i)

print(max(dp))


# # トポロジカルソート
# topol = []
# stack = []
# for i in range(N):
#     if indegree[i] == 0:
#         stack.append(i)

# while stack:
#     n = stack.pop()
#     topol.append(n)
#     for nxt in graph[n]:
#         indegree[nxt] -= 1
#         if indegree[nxt] == 0:
#             stack.append(nxt)

# rev = [0] * N
# for i in range(N):
#     rev[topol[i]] = i

# # dp[i] := topolのi番目までの最長経路の長さ
# dp = [0] * N
# for crr in topol:
#     for nxt in graph[crr]:
#         dp[rev[nxt]] = max(dp[rev[nxt]], dp[rev[crr]] + 1)

# print(max(dp))
