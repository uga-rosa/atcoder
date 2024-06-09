A, B, C, X = [int(input()) for _ in range(4)]

ans = 0
for i in range(A + 1):
    for j in range(B + 1):
        for k in range(C + 1):
            if 500 * i + 100 * j + 50 * k == X:
                ans += 1
print(ans)
