import sys


def main():
    N, M, K = LI()
    graph = [[] for _ in range(N)]
    for i in range(M):
        u, v = LI()
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)

    dp = MTX(K + 1, N)
    dp[0][0] = 1
    for i in range(K):
        s = sum(dp[i])
        for j in range(N):
            x = s - dp[i][j]
            for k in graph[j]:
                x -= dp[i][k]
            dp[i + 1][j] = x % 998244353

    print(dp[K][0])


# fmt: off
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def MTX(n, m, init=0): return [[init] * m for _ in range(n)]


if __name__ == "__main__":
    main()
