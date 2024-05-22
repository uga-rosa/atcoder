import sys

sys.setrecursionlimit(300000)


N = int(sys.stdin.readline().rstrip())
A, B = [0] * N, [0] * N
for i in range(N):
    A[i], B[i] = list(map(int, sys.stdin.readline().rstrip().split()))

# キーが盤面 (bit)、1が場に残っているカード
# 値はその盤面からゲームを始めて、Takahashiが勝つかどうかのbool
dp = [-1] * (1 << N)
for b in range(1 << N):
    f = 0
    for i in range(N - 1):
        for j in range(i + 1, N):
            if ((b >> i) & 1) and ((b >> j) & 1):
                if (A[i] == A[j] or B[i] == B[j]) and (
                    dp[b ^ (1 << i) ^ (1 << j)] == 0
                ):
                    f = 1
    dp[b] = f

print(dp[-1] and "Takahashi" or "Aoki")
