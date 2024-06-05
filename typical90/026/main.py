from collections import deque

N = int(input())
g = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

# 再帰だとTLEした
stack = deque()
stack.append((1, 0))
col = [-1] * (N+1)
while stack:
    pos, cur = stack.pop()
    col[pos] = cur
    for nxt in g[pos]:
        if col[nxt] == -1: stack.append((nxt, 1-cur))

zero, one = [], []
for i in range(N+1):
    if col[i] == 0: zero.append(i)
    elif col[i] == 1: one.append(i)

if len(one) >= N//2:
    print(*one[:N//2])
else:
    print(*zero[:N//2])
