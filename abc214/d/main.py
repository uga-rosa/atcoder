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


N = int(sys.stdin.readline().rstrip())
edges = []
for i in range(N - 1):
    u, v, w = list(map(int, sys.stdin.readline().rstrip().split()))
    edges.append((u - 1, v - 1, w))

edges.sort(key=lambda x: x[2])

uf = UnionFind(N)

ans = 0

for u, v, w in edges:
    ans += w * uf.size(u) * uf.size(v)
    uf.union(u, v)

print(ans)
