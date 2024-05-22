import bisect, collections, copy, heapq, itertools, math, numpy, string
import sys


def main(input):
    x = list(map(int, input))

    if all_same(x):
        print("Weak")
        return

    for i in range(1, len(x)):
        if not (x[i] == 0 and x[i - 1] == 9 or (x[i] == x[i - 1] + 1)):
            print("Strong")
            return
    print("Weak")


def all_same(l):
    for i in range(1, len(l)):
        if l[i] != l[i - 1]:
            return False
    return True


def InputInt():
    return int(sys.stdin.readline().rstrip())


def InputIntList():
    return list(map(int, sys.stdin.readline().rstrip().split()))


def InputStr():
    return sys.stdin.readline().rstrip()


def InputStrList():
    return list(sys.stdin.readline().rstrip().split())


if __name__ == "__main__":
    input = InputStr()
    main(input)
