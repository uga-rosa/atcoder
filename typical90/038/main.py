import math

L = 10**18
A, B = map(int, input().split())

l = math.lcm(A, B)
if l > L:
    print("Large")
else:
    print(l)
