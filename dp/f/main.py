import sys

sys.setrecursionlimit(300000)


s = sys.stdin.readline().rstrip()
t = sys.stdin.readline().rstrip()

# dp[i][j] := sのi文字目までとtのj文字目までの最長共通部分の長さ
dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
for i in range(len(s)):
    for j in range(len(t)):
        if s[i] == t[j]:
            dp[i + 1][j + 1] = dp[i][j] + 1
        dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i + 1][j], dp[i][j + 1])

# 長さから文字列を復元
i, j = len(s), len(t)
res = ""
while i > 0 and j > 0:
    if dp[i][j] == dp[i - 1][j]:
        i -= 1
    elif dp[i][j] == dp[i][j - 1]:
        j -= 1
    else:
        i -= 1
        j -= 1
        res = s[i] + res
print(res)
