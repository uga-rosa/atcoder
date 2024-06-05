import sys
sys.setrecursionlimit(300000)

N, M = list(map(int, sys.stdin.readline().rstrip().split()))
A = list(map(int, sys.stdin.readline().rstrip().split()))
B = list(map(int, sys.stdin.readline().rstrip().split()))
A.sort()
B.sort()

if N == 1:
    print("No")
    exit()
elif N-M > 1:
    print("Yes")
    exit()

if A[0] < B[0]:
    pre_grp, i, j = "A", 1, 0
else:
    pre_grp, i, j = "B", 0, 1

while i < N and j < M:
    if A[i] < B[j]:
        if pre_grp == "A":
            print("Yes")
            exit()
        i += 1
        pre_grp = "A"
    else:
        j += 1
        pre_grp = "B"
if pre_grp == "A":
    print("No")
else:
    if i == N-1:
        print("No")
    else:
        print("Yes")
