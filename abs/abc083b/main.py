N, A, B = map(int, input().split())

ans = 0
for i in range(1, N+1):
    s = sum(map(int, list(str(i))))
    if A <= s <= B:
        ans += i
print(ans)
