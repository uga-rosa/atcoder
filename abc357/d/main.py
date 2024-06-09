N = int(input())
MOD = 998244353
p10 = pow(10, len(str(N)), MOD)
print(N * (1 - pow(p10, N, MOD)) * pow(1 - p10, -1, MOD) % MOD)
