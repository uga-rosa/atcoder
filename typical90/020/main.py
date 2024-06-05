a, b, c = map(int, input().split())

# これは通らない。floatの誤差
# print(math.log2(a) < b * math.log2(c) and "Yes" or "No")

# a < c ** b を示せばいい
print(a < c**b and "Yes" or "No")
