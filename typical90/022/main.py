import math

a, b, c = map(int, input().split())

g = math.gcd(a, b, c)
print((a//g-1) + (b//g-1) + (c//g-1))
