from atcoder.mincostflow import MCFGraph

N, K = map(int, input().split())
B = 1<<32

g = MCFGraph(2*N+2)
start, goal = 2*N, 2*N+1

for i in range(N):
    for j, a in enumerate(map(int, input().split())):
        g.add_edge(i, j+N, 1, B-a)
    g.add_edge(start, i, K, 0)
    g.add_edge(i+N, goal, K, 0)
g.add_edge(start, goal, N*K, B)

_, min_cost = g.flow(start, goal, N*K)
grid = [["."] * N for _ in range(N)]
for edge in g.edges():
    if edge.src == start or edge.dst == goal or edge.flow == 0:
        continue
    grid[edge.src][edge.dst-N] = "X"

print(B*N*K-min_cost)
for i in range(N):
    print("".join(grid[i]))
