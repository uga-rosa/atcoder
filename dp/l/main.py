import sys
sys.setrecursionlimit(300000)

N = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().rstrip().split()))

# dp[i][j] := 閉区間[i, j]が残っているときの「次の手番の人の得点ーそうじゃない方の人の得点」
dp = [[-1] * N for _ in range(N)]
def rec(l, r):
    if dp[l][r] != -1: return dp[l][r]
    if l == r: dp[l][r] = a[l]
    else: dp[l][r] = max(a[l] - rec(l+1, r), a[r] - rec(l, r-1))
    return dp[l][r]
print(rec(0, N-1))
