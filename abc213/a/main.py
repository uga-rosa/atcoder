import sys


def main():
    A, B = LI()
    # if a == 0 and b == 0 then c == 0
    # if a == 0 and b == 1 then c == 1
    # if a == 1 and b == 0 then c == 1
    # if a == 1 and b == 1 then c == 0
    print(A ^ B)


# fmt: off
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def MTX(n, m, init=0): return [[init] * m for _ in range(n)]


if __name__ == "__main__":
    main()
