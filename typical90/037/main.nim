import sequtils, strutils

const size = 1 shl 14

var W, N: int
(W, N) = stdin.readLine.split.map(parseInt)

var data: seq[seq[int]]
for i in 0..<N:
  data.add(stdin.readLine.split.map(parseInt))

proc update(lst: var seq[int], pos: int, x: int) =
  var p = pos + size
  if lst[p] > x: return
  lst[p] = x
  while p > 1:
    p = p shr 1
    lst[p] = max(lst[2*p], lst[2*p+1])

proc getMax(lst: seq[int], ql, qr: int, sl = 0, sr = size, pos = 1): int =
  if sr <= ql or qr <= sl: return -1
  elif ql <= sl and sr <= qr: return lst[pos]
  else:
    let sm = (sl + sr) div 2
    let lmax = getMax(lst, ql, qr, sl, sm, 2*pos)
    let rmax = getMax(lst, ql, qr, sm, sr, 2*pos+1)
    return max(lmax, rmax)

# dp[i][j] := i番目までの料理で香辛料を丁度j使うときの価値の最大値
var dp = newSeqWith(N + 1, newSeqWith(2 * size, -1))

update(dp[0], 0, 0)

for i in 0..<N:
  let (l, r, v) = (data[i][0], data[i][1], data[i][2])
  for j in 0..W:
    var vmax = dp[i][j + size]
    let (sl, sr) = (max(j - r, 0), max(j - l + 1, 0))
    if sl != sr:
      let val = getMax(dp[i], sl, sr)
      if val != -1:
        vmax = max(vmax, val + v)
    update(dp[i + 1], j, vmax)

echo dp[N][W + size]
