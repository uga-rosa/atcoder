import math

N, Q = map(int, input().split())
coord = [[]] * N
x_max, x_min = 0, math.inf
y_max, y_min = 0, math.inf
for i in range(N):
    x, y = map(int, input().split())
    # 45度回転 + sqrt(2)拡大
    # 回転後の座標を使うと Manhattan distance は max(abs(x-x'), abs(y-y'))
    X, Y = x-y, x+y
    if X > x_max: x_max = X
    if X < x_min: x_min = X
    if Y > y_max: y_max = Y
    if Y < y_min: y_min = Y
    coord[i] = [X, Y]

for _ in range(Q):
    q = int(input()) - 1
    x, y = coord[q]
    print(max(x_max-x, x-x_min, y_max-y, y-y_min))
