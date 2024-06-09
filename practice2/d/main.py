from atcoder.maxflow import MFGraph

N, M = map(int, input().split())
S = [list(input()) for _ in range(N)]

# g[N*M] := start, g[N*M+1] := end
g = MFGraph(N*M+2)
s, e = N*M, N*M+1
for i in range(N):
    for j in range(i%2, M, 2):
        if S[i][j] == '#': continue
        idx = i*M + j
        g.add_edge(s, idx, 1)
        if i-1 >= 0 and S[i-1][j] == '.':
            g.add_edge(idx, idx-M, 1)
        if i+1 < N and S[i+1][j] == '.':
            g.add_edge(idx, idx+M, 1)
        if j-1 >= 0 and S[i][j-1] == '.':
            g.add_edge(idx, idx-1, 1)
        if j+1 < M and S[i][j+1] == '.':
            g.add_edge(idx, idx+1, 1)
    for j in range(1-i%2, M, 2):
        if S[i][j] == '#': continue
        idx = i*M + j
        g.add_edge(idx, e, 1)

print(g.flow(s, e))

for edge in g.edges():
    if edge.src == s or edge.dst == e or edge.flow == 0: continue
    si, sj = edge.src // M, edge.src % M
    di, dj = edge.dst // M, edge.dst % M
    if si < di:
        S[si][sj] = "v"
        S[di][dj] = "^"
    elif si > di:
        S[si][sj] = "^"
        S[di][dj] = "v"
    elif sj < dj:
        S[si][sj] = ">"
        S[di][dj] = "<"
    elif sj > dj:
        S[si][sj] = "<"
        S[di][dj] = ">"

for ss in S:
    print("".join(ss))
