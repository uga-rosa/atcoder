import bisect, collections, copy, heapq, itertools, math, numpy, string
import sys


def main():
    N, M = LI()
    A = LI()
    B = LI()

    A.sort()
    B.sort()

    i, j, ans = 0, 0, abs(A[0] - B[0])
    while i < N and j < M:
        ans = min(ans, abs(A[i] - B[j]))
        if A[i] < B[j]:
            i += 1
        else:
            j += 1

    print(ans)


# fmt: off
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())


if __name__ == "__main__":
    main()
