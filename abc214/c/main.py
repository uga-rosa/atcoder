import sys

sys.setrecursionlimit(300000)


N = int(sys.stdin.readline().rstrip())
S = list(map(int, sys.stdin.readline().rstrip().split()))
T = list(map(int, sys.stdin.readline().rstrip().split()))

for i in range(N * 2):
    T[(i + 1) % N] = min(T[(i + 1) % N], T[i % N] + S[i % N])

for i in range(N):
    print(T[i])
