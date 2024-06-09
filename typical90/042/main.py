K = int(input())
MOD = 10**9+7

# 9の倍数 = 各桁の和が9の倍数
if K % 9 != 0:
    print(0)
    exit()

# dp[i] := 各桁の総和がiであるものの数
dp = [0] * (K+1)
dp[0] = 1
for i in range(1, K+1):
    for j in range(1, min(i, 9) + 1):
        dp[i] += dp[i - j]
    dp[i] %= MOD

print(dp[K])
