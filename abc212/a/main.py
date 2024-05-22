import bisect, collections, copy, heapq, itertools, math, numpy, string
import sys


def main(input):
    A, B = input[0], input[1]
    if B == 0:
        print("Gold")
    elif A == 0:
        print("Silver")
    else:
        print("Alloy")


def InputInt():
    return int(sys.stdin.readline().rstrip())


def InputIntList():
    return list(map(int, sys.stdin.readline().rstrip().split()))


def InputStr():
    return sys.stdin.readline().rstrip()


def InputStrList():
    return list(sys.stdin.readline().rstrip().split())


if __name__ == "__main__":
    input = InputIntList()
    main(input)
