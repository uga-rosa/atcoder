import sys
sys.setrecursionlimit(300000)

MOD = 998244353
N, M = list(map(int, sys.stdin.readline().rstrip().split()))

res = 0
for i in range(62):
    if (M >> i) & 1:
        # 0からNまでの間に、i番目のbitが何回1になるか
        c = (N >> (i+1)) << i
        if N & (1<<i):
            c += (N & ((1<<i)-1)) + 1
        res += c
        res %= MOD
print(res)
