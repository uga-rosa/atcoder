import sys, math

sys.setrecursionlimit(300000)


MAX_V = 10**5 + 1
N, W = list(map(int, sys.stdin.readline().rstrip().split()))
w, v = [0] * (N + 1), [0] * (N + 1)
for i in range(N):
    w[i], v[i] = list(map(int, sys.stdin.readline().rstrip().split()))

# dp[ i ][ sum_v ] := i-1 番目までの品物から価値が sum_v となるように選んだときの、重さの総和の最小値
dp = [[math.inf] * (MAX_V) for _ in range(N + 1)]
dp[0][0] = 0

for i in range(N):
    for sum_v in range(MAX_V):
        if sum_v >= v[i]:
            dp[i + 1][sum_v] = min(dp[i][sum_v], dp[i][sum_v - v[i]] + w[i])
        else:
            dp[i + 1][sum_v] = dp[i][sum_v]

res = 0
for sum_v in range(MAX_V):
    if dp[N][sum_v] <= W:
        res = sum_v
print(res)
