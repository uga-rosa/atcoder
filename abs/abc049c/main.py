S = input()
i = len(S)
while i > 0:
    if i >= 7 and S[i-7:i] == "dreamer":
        i -= 7
    elif i >= 6 and S[i-6:i] == "eraser":
        i -= 6
    elif i >= 5 and (S[i-5:i] == "dream" or S[i-5:i] == "erase"):
        i -= 5
    else:
        break
print(i == 0 and "YES" or "NO")
