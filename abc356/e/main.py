from collections import Counter

N = int(input())
A = sorted(map(int, input().split()))
M = 10**6

cnt = [0] * (M+1)
for a in A:
    cnt[a] += 1
for i in range(len(cnt)-1):
    cnt[i+1] += cnt[i]

ans = 0
for a, t in Counter(A).items():
    # 同じ値だが自分ではない相手とのペア
    ans += t * (t-1) // 2
    for n in range(1, M // a + 1):
        c = cnt[min(M, a*(n+1)-1)] - cnt[a*n-1]
        if n == 1:
            c -= t
        ans += t * n * c

print(ans)
