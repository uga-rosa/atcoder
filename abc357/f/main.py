from atcoder.lazysegtree import LazySegTree
from dataclasses import dataclass

@dataclass
class S:
    Asum: int
    Bsum: int
    Sum: int

@dataclass
class F:
    Asum: int
    Bsum: int

L = 998244353

N, Q = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
D = [S(A[i], B[i], A[i]*B[i]%L) for i in range(N)]

def op(x: S, y: S):
    asum = x.Asum + y.Asum
    bsum = x.Bsum + y.Bsum
    sum = (x.Sum + y.Sum) % L
    return S(asum, bsum, sum)

# lazy -> data
def mapping(f: F, s: S):
    s.Asum += f.Asum // 2
    s.Bsum += f.Bsum // 2
    return s

# lazy -> lazy
def composition(f: F, g: F):
    g.Asum += f.Asum // 2
    g.Bsum += f.Bsum // 2
    return g

lst = LazySegTree(op, S(0, 0, 0), mapping, composition, F(0, 0), D)

for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        l, r, x = q[1:]
        lst.apply(l, r+1, lambda s: s.A + x)
    elif q[0] == 2:
        l, r, x = q[1:]
        lst.apply(l, r+1, lambda s: s.B + x)
    else:
        l, r = q[1:]
        print(lst.prod(l, r+1))
