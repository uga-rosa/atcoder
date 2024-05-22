import sys

sys.setrecursionlimit(300000)


H, W = list(map(int, sys.stdin.readline().rstrip().split()))
M = []
for _ in range(H):
    M.append(list(map(int, sys.stdin.readline().rstrip().split())))


M1 = [0] * W
M2 = [0] * H

for i in range(H):
    for j in range(W):
        M1[j] += M[i][j]
        M2[i] += M[i][j]

R = [[0] * W for _ in range(H)]
for i in range(H):
    for j in range(W):
        R[i][j] += M1[j]
        R[i][j] += M2[i]
        R[i][j] -= M[i][j]
    print(*R[i])
