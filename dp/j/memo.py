import sys
sys.setrecursionlimit(300000)

N = 10**2

dp = [-1] * (N+1)
def fib(x):
    if dp[x] != -1: return dp[x]
    if x == 0 or x == 1: return x
    dp[x] = fib(x-1) + fib(x-2)
    return dp[x]

print(fib(N))
