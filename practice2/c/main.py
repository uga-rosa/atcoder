from atcoder.math import floor_sum

T = int(input())
for _ in range(T):
    n, m, a, b = map(int, input().split())
    print(floor_sum(n, m, a, b))
