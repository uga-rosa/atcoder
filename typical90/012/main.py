import sys
sys.setrecursionlimit(300000)


class UnionFind:
    def __init__(self, n):
        self.par = [-1] * n
        self.rank = [0] * n
        self.siz = [1] * n

    def root(self, x):
        if self.par[x] == -1:
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    def issame(self, x, y):
        return self.root(x) == self.root(y)

    def union(self, x, y):
        rx, ry = self.root(x), self.root(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.par[ry] = rx
        self.rank[x] = max(self.rank[x], self.rank[ry] + 1)
        self.siz[rx] += self.siz[ry]
        return True

    def size(self, x):
        return self.siz[self.root(x)]


def id(r, c):
    return r * W + c


H, W = list(map(int, sys.stdin.readline().rstrip().split()))
uf = UnionFind(H*W)
isred = [[False] * W for _ in range(H)]
Q = int(sys.stdin.readline().rstrip())
for _ in range(Q):
    q = list(map(int, sys.stdin.readline().rstrip().split()))
    q = list(map(lambda x: x-1, q))
    if q[0] == 0:
        r, c = q[1:]
        isred[r][c] = True
        x = r * W + c
        if r > 0 and isred[r-1][c]: uf.union(x, id(r-1, c))
        if r < H-1 and isred[r+1][c]: uf.union(x, id(r+1, c))
        if c > 0 and isred[r][c-1]: uf.union(x, id(r, c-1))
        if c < W-1 and isred[r][c+1]: uf.union(x, id(r, c+1))
    else:
        ra, ca, rb, cb = q[1:]
        print(isred[ra][ca] and uf.issame(id(ra, ca), id(rb, cb)) and "Yes" or "No")
