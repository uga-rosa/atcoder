from collections import deque

H, W = map(int, input().split())
rs, cs = map(lambda x: int(x)-1, input().split())
rt, ct = map(lambda x: int(x)-1, input().split())
maze = [list(input()) for _ in range(H)]

D = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# ranks[i][j][d] := (i,j), 方向dまでに曲がる最小の数
ranks = [[[-1] * 4 for _ in range(W)] for _ in range(H)]
que = deque()
que.append((rs, cs, 0, 0))
que.append((rs, cs, 1, 0))
que.append((rs, cs, 2, 0))
que.append((rs, cs, 3, 0))
while que:
    i, j, d, rank = que.popleft()
    ranks[i][j][d] = rank
    if i == rt and j == ct:
        break
    ni, nj = i+D[d][0], j+D[d][1]
    if 0 <= ni < H and 0 <= nj < W and maze[ni][nj] == ".":
        for dd in range(4):
            if ranks[ni][nj][dd] != -1: continue
            if dd == d:
                que.appendleft((ni, nj, d, rank))
            else:
                que.append((ni, nj, dd, rank+1))

print(max(ranks[rt][ct]))
