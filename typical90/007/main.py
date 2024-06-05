import sys
sys.setrecursionlimit(300000)

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))
Q = int(sys.stdin.readline().rstrip())

A.sort()

def binary_search(x):
    l, r = -1, N
    while r - l > 1:
        mid = (l + r) // 2
        if A[mid] >= x: r = mid
        else: l = mid
    return r

for _ in range(Q):
    B = int(sys.stdin.readline().rstrip())
    i = binary_search(B)
    if i == 0:
        print(A[0] - B)
    elif i == N:
        print(B - A[N-1])
    else:
        print(min(A[i] - B, B - A[i-1]))
