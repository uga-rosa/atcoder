from atcoder.lazysegtree import LazySegTree

# (sum1, sum0, sumInv)
e = (0, 0, 0)
id_ = False

N, Q = map(int, input().split())
A = [a == '1' and (1, 0, 0) or (0, 1, 0) for a in input().split()]

def op(s, t):
    sum1s, sum0s, sumInvs = s
    sum1t, sum0t, sumInvt = t
    return sum1s+sum1t, sum0s+sum0t, sumInvs+sumInvt+sum1s*sum0t

# lazy -> data
def mapping(f, s):
    sum1s, sum0s, sumInvs = s
    if f:
        # 0と1のペアの総数に対して転倒数は反転する
        return sum0s, sum1s, (sum1s*sum0s) - sumInvs
    return sum1s, sum0s, sumInvs

# lazy -> lazy
def composition(f, g):
    if f:
        return not g
    return g

lst = LazySegTree(op, e, mapping, composition, id_, A)

for _ in range(Q):
    t, l, r = map(int, input().split())
    if t == 1:
        lst.apply(l-1, r, True)
    else:
        print(lst.prod(l-1, r)[2])
