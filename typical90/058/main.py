N, K = map(int, input().split())
MOD = 10**5

if N == 0:
    print(0)
    exit()

dig = lambda s: sum(map(int, str(s)))

M = 0
C = [-1] * MOD
Cinv = [-1] * MOD
for i in range(min(N, MOD) + 1):
    N = (N + dig(N)) % MOD
    if C[N] != -1:
        M = i - C[i]
        break
    C[N] = i
    Cinv[i] = N
    M = i

K %= M
print(Cinv[K-1])
