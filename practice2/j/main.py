from atcoder.segtree import SegTree

N, Q = map(int, input().split())
A = list(map(int, input().split()))

seg = SegTree(max, -1, A)
for _ in range(Q):
    t, x, y = map(int, input().split())
    if t == 1:
        seg.set(x-1, y)
    elif t == 2:
        print(seg.prod(x-1, y))
    else:
        print(seg.max_right(x-1, lambda p: p < y) + 1)
