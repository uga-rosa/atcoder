import sys
sys.setrecursionlimit(300000)

N, M = list(map(int, sys.stdin.readline().rstrip().split()))
A = list(map(int, sys.stdin.readline().rstrip().split()))

sum = [0] * M
for _ in range(N):
    x = list(map(int, sys.stdin.readline().rstrip().split()))
    for i in range(M):
        sum[i] += x[i]

for i in range(M):
    if sum[i] < A[i]:
        print("No")
        break
else:
    print("Yes")
