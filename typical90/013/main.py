import sys, heapq
sys.setrecursionlimit(300000)

N, M = list(map(int, sys.stdin.readline().rstrip().split()))
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = list(map(int, sys.stdin.readline().rstrip().split()))
    graph[a-1].append((b-1, c))
    graph[b-1].append((a-1, c))

def solve(s):
    score = [float('inf')] * N
    score[s] = 0
    que = []
    heapq.heappush(que, (0, s))
    while que:
        _, crr = heapq.heappop(que)
        for nxt, c in graph[crr]:
            if score[crr] + c < score[nxt]:
                score[nxt] = score[crr] + c
                heapq.heappush(que, (score[nxt], nxt))
    return score

score_from_0 = solve(0)
score_from_N = solve(N-1)
for k in range(N):
    print(score_from_0[k] + score_from_N[k])
