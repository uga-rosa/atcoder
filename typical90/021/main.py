# 強連結成分分解 (SCC)
N, M = map(int, input().split())
g = [[] for _ in range(N)]
gr = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    g[a-1].append(b-1)
    gr[b-1].append(a-1)

order = []
seen = [False] * N
def dfs(cur):
    seen[cur] = True
    for nxt in g[cur]:
        if not seen[nxt]: dfs(nxt)
    order.append(cur)

def dfs_rev(cur):
    pass
