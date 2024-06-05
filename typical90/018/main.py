import math

T = int(input())
L, X, Y = list(map(int, input().split()))
Q = int(input())

# 時刻 e における観覧車の座標 (0, y, z)
def coord(e):
    theta = (e % T) / T * 2 * math.pi
    return -math.sin(theta)*L/2, -math.cos(theta)*L/2 + L/2

# 俯角
# xy平面上での距離をlとすると、arctan(z/l)
def depre(y, z):
    l = math.sqrt(X**2 + (Y-y)**2)
    return math.degrees(math.atan(z/l))

for _ in range(Q):
    e = int(input())
    y, z = coord(e)
    print(depre(y, z))
