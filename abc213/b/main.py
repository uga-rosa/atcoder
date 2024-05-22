import sys


def main():
    N = I()
    A = LI()

    revA = {}
    for i in range(N):
        revA[A[i]] = i

    A.sort()
    print(revA[A[-2]] + 1)


# fmt: off
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def MTX(n, m, init=0): return [[init] * m for _ in range(n)]


if __name__ == "__main__":
    main()
