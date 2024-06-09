import math

H, W = map(int, input().split())

# こういうの
# #.#.#.#.#.
# ..........
# #.#.#.#.#.
# ..........
# ただしH, W=1のときは全部点灯できる
if H == 1:
    print(W)
elif W == 1:
    print(H)
else:
    print(math.ceil(H / 2) * math.ceil(W / 2))
