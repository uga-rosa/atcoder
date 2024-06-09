N = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)

alice, bob = 0, 0
for i in range(N):
    if i & 1: bob += a[i]
    else: alice += a[i]
print(alice - bob)
