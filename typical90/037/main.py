from atcoder.segtree import SegTree

W, N = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]

# dp[i][j] := i番目までの料理で香辛料を丁度j使うときの価値の最大値
dp = [SegTree(max, -1, W+1) for _ in range(N+1)]
dp[0].set(0, 0)

for i in range(N):
    l, r, v = data[i]
    for j in range(W+1):
        vmax = dp[i].get(j)
        sl, sr = max(j-r, 0), max(j-l+1, 0)
        if sl != sr:
            val = dp[i].prod(sl, sr)
            if val != -1:
                vmax = max(vmax, val+v)
        dp[i+1].set(j, vmax)

print(dp[N].get(W))
