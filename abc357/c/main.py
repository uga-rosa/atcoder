N = int(input())

around = [[0,0], [0,1], [0,2], [1,0], [1,2], [2,0], [2,1], [2,2]]

def rec(level):
    if level == 0: return [["#"]]
    g: list[list[str]] = [["."] * (3**level) for _ in range(3**level)]
    gg = rec(level-1)
    z = 3**(level-1)
    for i in range(z):
        for j in range(z):
            for k, l in around:
                g[i+z*k][j+z*l] = gg[i][j]
    return g

ans = rec(N)
for a in ans:
    print("".join(a))
