# 区間更新、区間最大値の取得
_, n = map(int, input().split())
w = 2**19
data = [0] * (2*w)
lazy = [0] * (2*w)

def propagate(pos):
    if lazy[pos] == 0: return
    lazy[2*pos] = lazy[2*pos+1] = data[2*pos] = data[2*pos+1] = lazy[pos]
    lazy[pos] = 0

def update(ql, qr, x, bl=0, br=w, pos=1):
    if br <= ql or qr <= bl:
        return
    elif ql <= bl and br <= qr:
        lazy[pos] = data[pos] = x
    else:
        propagate(pos)
        bm = (bl + br) // 2
        update(ql, qr, x, bl, bm, 2*pos)
        update(ql, qr, x, bm, br, 2*pos+1)
        data[pos] = max(data[2*pos], data[2*pos+1])

def get_max(ql, qr, bl=0, br=w, pos=1):
    if br <= ql or qr <= bl:
        return 0
    elif ql <= bl and br <= qr:
        return data[pos]
    else:
        propagate(pos)
        bm = (bl + br) // 2
        lmax = get_max(ql, qr, bl, bm, 2*pos)
        rmax = get_max(ql, qr, bm, br, 2*pos+1)
        return max(lmax, rmax)

for i in range(n):
    l, r = list(map(int, input().split()))
    h = get_max(l, r+1)
    print(h+1)
    update(l, r+1, h+1)
