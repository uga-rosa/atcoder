import sys

sys.setrecursionlimit(300000)

H, W = list(map(int, sys.stdin.readline().rstrip().split()))
mtx = []
for _ in range(H):
    mtx.append(list(sys.stdin.readline().rstrip()))

start = (0, 0)
goal = (H - 1, W - 1)
