from atcoder.fenwicktree import FenwickTree

N, Q = map(int, input().split())
f = FenwickTree(N)
for i, a in enumerate(map(int, input().split())):
    f.add(i, a)

for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 0:
        p, x = q[1:]
        f.add(p, x)
    else:
        l, r = q[1:]
        print(f.sum(l, r))
