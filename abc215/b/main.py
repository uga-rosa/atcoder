import sys
sys.setrecursionlimit(300000)


N = int(sys.stdin.readline().rstrip())
k = 0
while N >= 2:
    k += 1
    N //= 2
print(k)
