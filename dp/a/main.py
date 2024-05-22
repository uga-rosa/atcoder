import sys, math

sys.setrecursionlimit(300000)


N = int(sys.stdin.readline().rstrip())
h = list(map(int, sys.stdin.readline().rstrip().split()))
h.extend([0, 0])

dp = [math.inf] * (N + 2)
dp[0] = 0
for i in range(N - 1):
    dp[i + 1] = min(dp[i + 1], dp[i] + abs(h[i + 1] - h[i]))
    dp[i + 2] = min(dp[i + 2], dp[i] + abs(h[i + 2] - h[i]))
print(dp[N - 1])
