import sys, heapq
sys.setrecursionlimit(300000)

N, K = list(map(int, sys.stdin.readline().rstrip().split()))
S = sys.stdin.readline().rstrip()

q = []
heapq.heapify(q)
next = -1
ans = ""
for i in range(N):
    heapq.heappush(q, (S[i], i))
    if i+K >= N:
        while 1:
            c, j = heapq.heappop(q)
            if j > next:
                ans += c
                next = j
                break
print(ans)
