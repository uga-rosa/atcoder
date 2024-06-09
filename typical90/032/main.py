import itertools, math

N = int(input())
A = [[]] * N
for i in range(N):
    A[i] = list(map(int, input().split()))
M = int(input())
g = [set() for _ in range(N)]
for _ in range(M):
    x, y = map(lambda x: int(x)-1, input().split())
    g[x].add(y)
    g[y].add(x)

# N <= 10なので全探索して10!でいい
ans = math.inf
for x in itertools.permutations(range(N)):
    sum = 0
    for i, v in enumerate(x):
        sum += A[v][i]
        if i > 0 and x[i-1] in g[v]:
            break
    else:
        ans = min(ans, sum)
print(math.isinf(ans) and -1 or ans)
