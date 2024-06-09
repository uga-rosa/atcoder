N = int(input())
p = [0, 0, 0]
for _ in range(N):
    t, x, y = map(int, input().split())
    time = t - p[0]
    dist = abs(x - p[1]) + abs(y - p[2])
    if time >= dist and (time - dist) % 2 == 0:
        p = [t, x, y]
    else:
        print("No")
        break
else:
    print("Yes")
