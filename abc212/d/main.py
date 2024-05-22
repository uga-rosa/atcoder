import bisect, collections, copy, heapq, itertools, math, numpy, string
import sys


def main():
    Q = I()
    h = []
    heapq.heapify(h)
    sum = 0
    for _ in range(Q):
        i = LI()
        if len(i) == 2:
            P, X = i
            if P == 1:
                heapq.heappush(h, X - sum)
            else:
                sum += X
        else:
            # Pi = 3
            print(heapq.heappop(h) + sum)


# fmt: off
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())


if __name__ == "__main__":
    main()
