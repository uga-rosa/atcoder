import sys

sys.setrecursionlimit(300000)


N, W = list(map(int, sys.stdin.readline().rstrip().split()))
w, v = [0] * N, [0] * N
for i in range(N):
    w[i], v[i] = list(map(int, sys.stdin.readline().rstrip().split()))

dp = [[0] * (W + 1) for _ in range(N)]
for i in range(w[0], W + 1):
    dp[0][i] = v[0]

for i in range(1, N):
    for j in range(W + 1):
        if j >= w[i]:
            dp[i][j] = max(dp[i - 1][j], (dp[i - 1][j - w[i]] + v[i]))
        else:
            dp[i][j] = dp[i - 1][j]
print(dp[N - 1][W])
