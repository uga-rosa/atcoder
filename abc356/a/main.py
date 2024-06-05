import sys
sys.setrecursionlimit(300000)

N, L, R = list(map(int, sys.stdin.readline().rstrip().split()))

a = []
for i in range(1, L):
    a.append(i)
for i in range(R, L-1, -1):
    a.append(i)
for i in range(R+1, N+1):
    a.append(i)
print(*a)
