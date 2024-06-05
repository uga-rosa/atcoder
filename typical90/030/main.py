N, K = map(int, input().split())

isPrime = [True] * (N+1)
for i in range(2, N+1):
    if not isPrime[i]: continue
    for j in range(i*2, N+1, i):
        isPrime[j] = False

c = [0] * (N+1)
for i in range(2, N+1):
    if not isPrime[i]: continue
    for j in range(i, N+1, i):
        c[j] += 1

ans = 0
for cc in c:
    if cc >= K: ans += 1
print(ans)
