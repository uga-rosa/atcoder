N, T, MOD = list(map(int, input().split()))

frak = [1] * (T+1)
for i in range(2, T+1):
    frak[i] = frak[i-1] * i % MOD

# comb[k] := comb(T, k) を事前計算
comb = [0] * (T+1)
for i in range(T+1):
    comb[i] = frak[T] * pow(frak[i], -1, MOD) * pow(frak[T-i], -1, MOD) % MOD

ans = 0
for _ in range(N):
    x, y = map(lambda x: abs(int(x)), input().split())
    i = (x - y + T) // 2
    j = (x + y + T) // 2
    ans = (ans + comb[i] * comb[j]) % MOD

print(ans)
