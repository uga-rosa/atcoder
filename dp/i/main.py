import sys

sys.setrecursionlimit(300000)


N = int(sys.stdin.readline().rstrip())
p = list(map(float, sys.stdin.readline().rstrip().split()))

if N == 1:
    print(p[0])
    sys.exit()

# dp[i][j] := コインi枚まで投げたとき表がj枚の確率
# O(N^2)
dp = [[0.0] * (N + 1) for _ in range(N)]
dp[0][0], dp[0][1] = 1 - p[0], p[0]
for i in range(1, N):
    for j in range(i + 2):
        dp[i][j] = dp[i - 1][j - 1] * p[i] + dp[i - 1][j] * (1 - p[i])

prob = 0
for i in range((N // 2) + 1, N + 1):
    prob += dp[N - 1][i]
print(prob)
