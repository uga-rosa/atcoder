import sys
sys.setrecursionlimit(300000)


S = sys.stdin.readline().rstrip()
print(S == "Hello,World!" and "AC" or "WA")
