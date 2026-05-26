S = input().strip()

i = 0
result = []

while i < len(S):
    if S[i] == 'S':
        result.append("send")
        i += 1
    elif S[i:i+2] == '[]':
        result.append("the")
        i += 2
    elif S[i:i+5] == '[sps]':
        result.append("ships")
        i += 5
    else:
        i += 1

print(" ".join(result))