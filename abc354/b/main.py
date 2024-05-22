import sys

sys.setrecursionlimit(300000)


N = int(sys.stdin.readline().rstrip())
users = []
T = 0
for _ in range(N):
    s, c = list(sys.stdin.readline().rstrip().split())
    users.append(s)
    T += int(c)

users.sort()
print(users[T % N])
