import sys

sys.setrecursionlimit(300000)

N, L = list(map(int, sys.stdin.readline().rstrip().split()))
K = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))
A.append(L)


def solve(M):
    pre, cnt = 0, 0
    for i in range(N + 1):
        if A[i] - pre >= M:
            cnt += 1
            if cnt > K:
                return True
            pre = A[i]
    return False


l, r = -1, L + 1
while abs(l - r) > 1:
    mid = (r + l) // 2
    if solve(mid):
        l = mid
    else:
        r = mid
print(l)
