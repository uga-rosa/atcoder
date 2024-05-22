import sys

sys.setrecursionlimit(300000)


S, T = list(map(int, sys.stdin.readline().rstrip().split()))
s = 0
for a in range(S + 1):
    for b in range(S - a + 1):
        for c in range(S - a - b + 1):
            if a * b * c <= T:
                s += 1
print(s)
