import sys

sys.setrecursionlimit(300000)


A, B, C, D = list(map(int, sys.stdin.readline().rstrip().split()))

p = (A, B)
w, h = C - A, D - B

# 1*1の黒面積(*2)
s = [[2, 1], [1, 2], [0, 1], [1, 0]]

# 横に切ると2層の繰り返し
layer = [0] * 2
c = [w // 4] * 4
for j in range(w % 4):
    c[(A + j) % 4] += 1
for i in range(2):
    for j, k in enumerate(c):
        layer[i] += k * s[j][i]

layer_n = [h // 2] * 2
if h % 2 == 1:
    layer_n[B % 2] += 1

S = layer[0] * layer_n[0] + layer[1] * layer_n[1]
print(S)
