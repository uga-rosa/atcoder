# TLEする
from atcoder.convolution import convolution

N, M = list(map(int, input().split()))
MOD = 998244353
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(*convolution(MOD, A, B))

# 多倍長整数でやろうとした残骸
# N, M = list(map(int, input().split()))
# k = 16
# K = (1 << k) - 1
# MOD = 998244353
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))

# nu = lambda L: int("".join([bin(K+a)[-k:] for a in L[::-1]]), 2)
# st = lambda n: bin(n)[2:] + "0"
# li = lambda s: [int(a, 2) if len(a) else 0 for a in [s[-(i+1)*k-1:-i*k-1] for i in range(len(A)+len(B)-1)]]

# print(*li(st(nu(A) * nu(B)))[1:])
