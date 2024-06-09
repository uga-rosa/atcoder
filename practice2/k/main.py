from atcoder.lazysegtree import LazySegTree

MOD = 998244353

# (value, length)
e = (0, 0)
# (b, c)
_id = (1, 0)

N, Q = map(int, input().split())
a = list(map(lambda x: (int(x), 1), input().split()))

def op(x, y):
    return (x[0] + y[0]) % MOD, x[1] + y[1]

# lazy -> data
def mapping(f, s):
    return (f[0] * s[0] + f[1] * s[1]) % MOD, s[1]

# lazy -> lazy
def composition(f, g):
    return (f[0] * g[0]) % MOD, (f[0] * g[1] + f[1]) % MOD

lst = LazySegTree(op, e, mapping, composition, _id, a)

for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 0:
        l, r, b, c = q[1:]
        lst.apply(l, r, (b, c))
    else:
        l, r = q[1:]
        print(lst.prod(l, r)[0])
