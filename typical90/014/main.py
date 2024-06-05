import sys
sys.setrecursionlimit(300000)

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))
B = list(map(int, sys.stdin.readline().rstrip().split()))
A.sort()
B.sort()

sum = 0
for i in range(N):
    sum += abs(A[i] - B[i])
print(sum)
