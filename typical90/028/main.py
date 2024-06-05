N = int(input())
M = 1010
p = [[0] * M for _ in range(M)]
for _ in range(N):
    lx, ly, rx, ry = map(int, input().split())
    p[lx][ly] += 1
    p[lx][ry] -= 1
    p[rx][ly] -= 1
    p[rx][ry] += 1

for i in range(1, M):
    for j in range(M):
        p[i][j] += p[i-1][j]
for i in range(M):
    for j in range(1, M):
        p[i][j] += p[i][j-1]

A = [0] * (N+1)
for x in range(M):
    for y in range(M):
        cnt = p[x][y]
        if cnt > 0: A[cnt] += 1

for i in range(1, N+1):
    print(A[i])
