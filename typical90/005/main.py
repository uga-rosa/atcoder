import sys, math

sys.setrecursionlimit(300000)


MOD = 10**9 + 7

N, B, K = list(map(int, sys.stdin.readline().rstrip().split()))
c = list(map(int, sys.stdin.readline().rstrip().split()))

# 小課題1まで通る
# 余りを持って桁DP
#
# dp = [[0] * B for _ in range(N + 1)]
# dp[0][0] = 1
# for i in range(N):
#     for j in range(B):
#         for k in range(K):
#             nxt = (10 * j + c[k]) % B
#             dp[i + 1][nxt] += dp[i][j]
#             dp[i + 1][nxt] %= MOD
#
# print(dp[N][0])


# 小課題2まで通る
# 同じ遷移のDPは行列累乗
#
# A = [[0] * B for _ in range(B)]
# for i in range(B):
#     for j in range(B):
#         for cc in c:
#             A[i][j] += (10 * i + cc) % B == j
#
#
# def mat_mul(a, b):
#     I, J, K = len(a), len(b[0]), len(b)
#     res = [[0] * J for _ in range(I)]
#     for i in range(I):
#         for j in range(J):
#             for k in range(K):
#                 res[i][j] += a[i][k] * b[k][j]
#             res[i][j] %= MOD
#     return res
#
#
# def mat_pow(x, n):
#     y = [[0] * len(x) for _ in range(len(x))]
#     for i in range(len(x)):
#         y[i][i] = 1
#     while n > 0:
#         if n & 1:
#             y = mat_mul(x, y)
#         x = mat_mul(x, x)
#         n >>= 1
#     return y
#
#
# def transpose(x):
#     if type(x[0]) == list:
#         I, J = len(x), len(x[0])
#         t = [[0] * I for _ in range(J)]
#         for i in range(I):
#             for j in range(J):
#                 t[j][i] = x[i][j]
#         return t
#     else:
#         I = len(x)
#         t = [[0] for _ in range(I)]
#         for i in range(I):
#             t[i][0] = x[i]
#         return t
#
#
# A_N = mat_pow(A, N)
# S = transpose([0] * B)
# S[0][0] = 1
# R = mat_mul(A_N, S)
# print(R[0][0])


# 小課題3まで通る
# ダブリング

# power10[i] = 10**2**i % B
# log_2(10**18) = 59.79..
logN = math.ceil(math.log2(N))
power10 = [10] * logN
for i in range(1, logN):
    power10[i] = (power10[i - 1] * power10[i - 1]) % B


dp = [[0] * B for _ in range(logN + 1)]
for cc in c:
    dp[0][cc % B] += 1
for i in range(1, logN):
    for j in range(B):
        for k in range(B):
            nxt = (j * power10[i] + k) % B
            dp[i + 1][nxt] += dp[i][j] * dp[i][k]
            dp[i + 1][nxt] %= MOD

print(dp)
print(dp[-1][0])
