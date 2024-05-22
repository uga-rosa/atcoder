import sys, math

sys.setrecursionlimit(300000)


H = int(sys.stdin.readline().rstrip())
i = 1
while H > 0:
    H -= 2**i
    i += 1
print(i)
