import sys

sys.setrecursionlimit(300000)


N = int(sys.stdin.readline().rstrip())


if N % 2 == 1:
    print("")
    sys.exit()


def ok(S):
    c = 0
    for s in S:
        c += s == "(" and 1 or -1
        if c < 0:
            return False
    return c == 0


for i in range(1 << N):
    s = ""
    for j in range(N):
        s = (((i >> j) & 1) and ")" or "(") + s
    if ok(s):
        print(s)
