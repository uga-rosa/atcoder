import sys

sys.setrecursionlimit(300000)


N = int(sys.stdin.readline().rstrip())
Cards = []
for i in range(N):
    a, c = list(map(int, sys.stdin.readline().rstrip().split()))
    Cards.append((a, c, i + 1))

Cards.sort(reverse=True)

i = 1
cost = Cards[0][1]
remain = []
for i in range(N):
    if Cards[i][1] <= cost:
        cost = Cards[i][1]
        remain.append(Cards[i][2])

remain.sort()
print(len(remain))
print(*remain)
