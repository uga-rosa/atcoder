N = int(input())

def dfs(crr, buf):
    if crr == N:
        print(buf)
        return

    for i in range(len(set(buf)) + 1):
        c = chr(0x61 + i)
        dfs(crr+1, buf+c)

dfs(0, "")
