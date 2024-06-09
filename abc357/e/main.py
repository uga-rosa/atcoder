from atcoder.scc import SCCGraph
from functools import cache

N = int(input())
a = list(map(lambda x: int(x)-1, input().split()))

g = SCCGraph(N)
for i in range(N):
    g.add_edge(i, a[i])

scc = g.scc()

# mapping[i] := 頂点iが属するsccの成分idx
mapping = [0] * N
for i, sc in enumerate(scc):
    for s in sc:
        mapping[s] = i

# SCCの成分が閉じてるかどうか
def close(lst: list[int]) -> bool:
    if len(lst) > 1: return True
    else: return a[lst[0]] == lst[0]

@cache
def count(i: int):
    if close(scc[i]):
        return len(scc[i])
    else:
        nxt = mapping[a[scc[i][0]]]
        return count(nxt) + 1

ans = 0
for i in range(len(scc)):
    c = count(i)
    ans += len(scc[i]) * c

print(ans)
