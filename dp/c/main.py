import sys

sys.setrecursionlimit(300000)


N = int(sys.stdin.readline().rstrip())
a, b, c = [0] * N, [0] * N, [0] * N
for i in range(N):
    a[i], b[i], c[i] = list(map(int, sys.stdin.readline().rstrip().split()))

dp = [[0] * 3 for _ in range(N)]
dp[0] = [a[0], b[0], c[0]]
for i in range(1, N):
    dp[i][0] = max(dp[i][0], dp[i - 1][1] + a[i], dp[i - 1][2] + a[i])
    dp[i][1] = max(dp[i][1], dp[i - 1][0] + b[i], dp[i - 1][2] + b[i])
    dp[i][2] = max(dp[i][2], dp[i - 1][0] + c[i], dp[i - 1][1] + c[i])
print(max(dp[N - 1]))
