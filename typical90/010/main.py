import sys
sys.setrecursionlimit(300000)

N = int(sys.stdin.readline().rstrip())
C, P = [0] * N, [0] * N
for i in range(N):
    C[i], P[i] = list(map(int, sys.stdin.readline().rstrip().split()))
# 累積和
S1 = [0] * (N+1)
S2 = [0] * (N+1)
if C[0] == 1: S1[0] = P[0]
else: S2[0] = P[0]
for i in range(1, N):
    S1[i] += S1[i-1]
    S2[i] += S2[i-1]
    if C[i] == 1: S1[i] += P[i]
    else: S2[i] += P[i]

Q = int(sys.stdin.readline().rstrip())
for _ in range(Q):
    l, r = list(map(int, sys.stdin.readline().rstrip().split()))
    l -= 1
    r -= 1
    # S1, S2は長さN+1にしてあるので、S1[-1] = S1[N] = 0になる
    print(S1[r]-S1[l-1], S2[r]-S2[l-1])
