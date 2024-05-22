import sys, math

sys.setrecursionlimit(300000)


N, K = list(map(int, sys.stdin.readline().rstrip().split()))
h = list(map(int, sys.stdin.readline().rstrip().split()))

dp = [math.inf] * N
dp[0] = 0
for i in range(N):
    for j in range(i + 1, min(i + K + 1, N)):
        dp[j] = min(dp[j], dp[i] + abs(h[i] - h[j]))

print(dp[N - 1])
