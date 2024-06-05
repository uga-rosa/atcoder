N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

mini_k = 0
for i in range(N):
    mini_k += abs(A[i] - B[i])
print((K >= mini_k and (K - mini_k) % 2 == 0) and "Yes" or "No")
