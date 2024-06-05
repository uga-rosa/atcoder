import sys
sys.setrecursionlimit(300000)

N, M, K = list(map(int, sys.stdin.readline().rstrip().split()))
# Nが小さいしビットで探索ぽい
b = 1 << N

Q = [[]] * M
for i in range(M):
    line = list(sys.stdin.readline().rstrip().split())
    r = line.pop()
    a = list(map(int, line[1:]))
    Q[i] = [a, r == 'o']

def ok(b):
    for a, r in Q:
        c = 0
        for aa in a:
            if b & (1 << (aa-1)):
                c += 1
        if (c >= K) != r:
            return False
    return True

sum = 0
for b in range(1 << N):
    if ok(b): sum += 1
print(sum)
