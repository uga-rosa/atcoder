import sys
sys.setrecursionlimit(300000)

N = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().rstrip().split()))

# dp[i][j][k] := 寿司が残り1個の皿がi枚、2個の皿がj枚、3個の皿が
# k枚の状態から、寿司を全てなくすのに必要な操作回数の期待値

dp = [[[-1] * (N+2) for _ in range(N+2)] for _ in range(N+2)]
def rec(i, j, k):
    if dp[i][j][k] != -1:
        return dp[i][j][k]
    if i == 0 and j == 0 and k == 0:
        return 0.0

    # dp[i][j][k] = 1 + (N-i-j-k)/N * dp[i][j][k] + i/N * dp[i-1][j][k] + j/N * dp[i+1][j-1][k] + k/N * dp[i][j+1][k-1]
    # dp[i][j][k] = N/(i+j+k) * ( 1 + i/N * dp[i-1][j][k] + j/N * dp[i+1][j-1][k] + k/N * dp[i][j+1][k-1] )
    #             = 1/(i+j+k) * ( N + i * dp[i-1][j][k] + j * dp[i+1][j-1][k] + k * dp[i][j+1][k-1] )
    res = 0.0
    if i > 0: res += i * rec(i-1, j, k)
    if j > 0: res += j * rec(i+1, j-1, k)
    if k > 0: res += k * rec(i, j+1, k-1)
    res += N
    res *= 1/(i+j+k)
    dp[i][j][k] = res
    return res

i, j, k = 0, 0, 0
for aa in a:
    if aa == 1:
        i += 1
    elif aa == 2:
        j += 1
    else:
        k += 1
print(rec(i, j, k))
