import sys


def main():
    H, W, N = LI()
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = LI()

    sortedA = sorted(list(set(A)))
    scoreA = {v: k for k, v in enumerate(sortedA)}
    resA = [scoreA[a] for a in A]
    sortedB = sorted(list(set(B)))
    scoreB = {v: k for k, v in enumerate(sortedB)}
    resB = [scoreB[b] for b in B]

    for i in range(N):
        print(resA[i] + 1, resB[i] + 1)


# fmt: off
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def MTX(n, m, init=0): return [[init] * m for _ in range(n)]


if __name__ == "__main__":
    main()
