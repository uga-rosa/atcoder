N = int(input())
A = list(map(int, input().split()))

flag = 0
ans = 0
while 1:
    for i in range(N):
        if A[i] & 1:
            flag = 1
            break
        A[i] >>= 1
    if flag:
        break
    ans += 1

print(ans)
