import sys
sys.setrecursionlimit(300000)


N = int(sys.stdin.readline().rstrip())
if N <= 125:
    print(4)
elif N <= 211:
    print(6)
else:
    print(8)
