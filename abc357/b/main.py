S = input()

lc = sum([c.islower() for c in S])
uc = sum([c.isupper() for c in S])

if lc > uc:
    print(S.lower())
else:
    print(S.upper())
