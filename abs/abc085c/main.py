N, Y = map(int, input().split())

for i in range(Y // 10000 + 1):
    for j in range((Y - 10000*i) // 5000 + 1):
        k = N - i - j
        if 10000*i + 5000*j + 1000*k == Y:
            print(i, j, k)
            exit()
print(-1, -1, -1)
