n = int(input())
a = list(map(int, input().split()))
a.sort()

def binary_search(n, isok):
    ng, ok = -1, n
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if isok(mid):
         ok = mid
        else:
            ng = mid
    return ok

MOD = 10**8
sum = 0
for i in range(n):
    sum += (n-1) * a[i]
    j = binary_search(n, lambda x: a[x] >= MOD-a[i])
    j = max(j, i+1)
    sum -= (n-j) * MOD
print(sum)
