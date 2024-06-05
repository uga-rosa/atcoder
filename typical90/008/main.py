import sys
sys.setrecursionlimit(300000)

T = "atcoder"
MOD = 10**9 + 7

def add(a, b):
    a += b
    if a >= MOD:
        a %= MOD
    return a

N = int(sys.stdin.readline().rstrip())
S = sys.stdin.readline().rstrip()

# dp[i][j] := 文字列Sの最初のi文字から何文字か抜き出してつなげる方法のうち、
# それが"atcoder"の最初のj文字まで一致するような場合の数
dp = [[0] * (len(T)+1) for _ in range(N+1)]
dp[0][0] = 1

for i in range(N):
    for j in range(len(T)+1):
        # S[i]を使わない
        dp[i+1][j] = add(dp[i+1][j], dp[i][j])
        # S[i]を使う
        if j < len(T) and S[i] == T[j]:
            dp[i+1][j+1] = add(dp[i+1][j+1], dp[i][j])

print(dp[N][len(T)])
