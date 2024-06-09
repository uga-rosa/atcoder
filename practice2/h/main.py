from atcoder.twosat import TwoSAT

# XにおくのをTrue, YにおくのをFalse
# 全ての2つの旗の組み合わせで、距離がD未満になってはいけない
N, D = list(map(int, input().split()))
Flag = [list(map(int, input().split())) for _ in range(N)]

twosat = TwoSAT(N)
for i in range(N-1):
    for j in range(i+1, N):
        # 全ての旗の組み合わせ
        if abs(Flag[i][0] - Flag[j][0]) < D:
            twosat.add_clause(i, False, j, False)
        if abs(Flag[i][0] - Flag[j][1]) < D:
            twosat.add_clause(i, False, j, True)
        if abs(Flag[i][1] - Flag[j][0]) < D:
            twosat.add_clause(i, True, j, False)
        if abs(Flag[i][1] - Flag[j][1]) < D:
            twosat.add_clause(i, True, j, True)

if twosat.satisfiable():
    print("Yes")
    ans = twosat.answer()
    for i in range(N):
        if ans[i]:
            print(Flag[i][0])
        else:
            print(Flag[i][1])
else:
    print("No")
