from atcoder.string import suffix_array, lcp_array
S = input()

ans = len(S) * (len(S) + 1) // 2
sa = suffix_array(S)
for x in lcp_array(S, sa):
    ans -= x
print(ans)
