N = int(input())
exists = set()
for i in range(N):
    s = input()
    if s in exists:
        continue
    else:
        exists.add(s)
        print(i+1)
