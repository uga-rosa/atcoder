import sys
sys.setrecursionlimit(300000)

A, B = list(map(int, sys.stdin.readline().rstrip().split()))
if A != B:
    for i in range(1, 4):
        if i != A and i != B: print(i)
else:
    print(-1)
