import sys, heapq
from collections import defaultdict

sys.setrecursionlimit(300000)


T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    d = defaultdict(list)
    for _ in range(N):
        l, r = list(map(int, sys.stdin.readline().rstrip().split()))
        d[l].append(r)
    ll = sorted(d.keys())

    q = []
    now = 1
    flag = True
    for l in ll:
        if not flag:
            break
        now = max(now, l)
        for r in d[now]:
            heapq.heappush(q, r)
        while q:
            r = heapq.heappop(q)
            if r >= now:
                now += 1
                for r in d[now]:
                    heapq.heappush(q, r)
            else:
                flag = False
                break

    print(flag and "Yes" or "No")
