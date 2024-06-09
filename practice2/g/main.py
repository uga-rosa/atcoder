from atcoder.scc import SCCGraph

N, M = list(map(int, input().split()))
g = SCCGraph(N)
for _ in range(M):
    a, b = map(int, input().split())
    g.add_edge(a, b)

scc = g.scc()
print(len(scc))
for s in scc:
    print(len(s), *s)
