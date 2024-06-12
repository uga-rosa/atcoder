N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

ma = [0] * 46
mb = [0] * 46
mc = [0] * 46
for i in range(N):
    ma[A[i] % 46] += 1
    mb[B[i] % 46] += 1
    mc[C[i] % 46] += 1

ans = 0
for i in range(46):
    for j in range(46):
        for k in range(46):
            if (i + j + k) % 46 == 0:
                ans += ma[i] * mb[j] * mc[k]
print(ans)
