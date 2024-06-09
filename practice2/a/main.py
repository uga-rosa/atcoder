from atcoder.dsu import DSU

N, Q = map(int, input().split())
dsu = DSU(N)
for _ in range(Q):
    t, u, v = map(int, input().split())
    if t == 0:
        dsu.merge(u, v)
    else:
        print(int(dsu.same(u, v)))
