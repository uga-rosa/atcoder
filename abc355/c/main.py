import sys
sys.setrecursionlimit(300000)

N, T = list(map(int, sys.stdin.readline().rstrip().split()))
A = list(map(int, sys.stdin.readline().rstrip().split()))

row = [0] * N
col = [0] * N
diagonal = [0] * 2
for t, a in enumerate(A):
    i, j = (a-1) // N, (a-1) % N
    row[i] += 1
    col[j] += 1
    if i == j: diagonal[0] += 1
    if i+j == N-1: diagonal[1] += 1
    if row[i] == N or col[j] == N or diagonal[0] == N or diagonal[1] == N:
        print(t+1)
        break
else:
    print(-1)
