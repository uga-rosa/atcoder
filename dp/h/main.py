import sys

sys.setrecursionlimit(300000)


H, W = list(map(int, sys.stdin.readline().rstrip().split()))
a = [[]] * H
for i in range(H):
    a[i] = list(sys.stdin.readline().rstrip())

# dp[i][j] := (i,j)までの経路総数
dp = [[0] * W for _ in range(H)]
dp[0][0] = 1
for i in range(H):
    for j in range(W):
        if i + j != 0 and a[i][j] == ".":
            dp[i][j] = (i > 0 and dp[i - 1][j] or 0) + (j > 0 and dp[i][j - 1] or 0)
            dp[i][j] %= 10**9 + 7

print(dp[H - 1][W - 1])
