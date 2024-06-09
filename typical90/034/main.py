from collections import defaultdict

N, K = map(int, input().split())
a = list(map(int, input().split()))

# [l, r)
r = 0
d = defaultdict(int)
ans = 0

for l in range(N):
    while r < N and len(d) + int(a[r] not in d) <= K:
        d[a[r]] += 1
        r += 1
    ans = max(ans, r-l)
    d[a[l]] -= 1
    if d[a[l]] <= 0: del d[a[l]]

print(ans)
