import sys, math
sys.setrecursionlimit(300000)

N = int(sys.stdin.readline().rstrip())
coins = list(map(int, sys.stdin.readline().rstrip().split()))
# 大きい順に A, B, C
coins.sort(reverse=True)
A, B, C = coins

def ext_gcd(a, b):
    if a == 0: return b, 0, 1
    gcd, x1, y1 = ext_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

# B, C の gcd
g = math.gcd(B, C)
# 一般解は (x, y) = (x0 + C/g k, y0 - B/g k)
_, x0, y0 = ext_gcd(B, C)

s = math.inf
for i in range(N // A + 1):
    r = N - A*i
    if r % g != 0:
        continue
    # 不定方程式 B x + C y = r の一般解は
    # (x, y) = (x0 * r/g + C/g*k, y0 * r/g - B/g*k)
    # kについて解くと
    # x0 * r/g + C/g k > 0 <=> k > g/C * (-x0 * r/g) = -x0 * r/C
    # y0 * r/g - B/g k > 0 <=> k < g/B * (y0 * r/g) = y0 * r/B
    min_k = math.ceil(-x0 * r/C)
    max_k = math.floor(y0 * r/B)
    for k in range(min_k, max_k+1):
        x, y = x0 * r//g + C//g*k, y0 * r//g - B//g*k
        s = min(s, i + x + y)

print(s)
