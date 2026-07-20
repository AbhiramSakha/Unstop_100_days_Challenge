def user_logic(n, s):
    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in s:
        if freq[ch] == 1:
            return ch

    return "-1"


import sys
input = sys.stdin.read

data = input().strip().split()

n = int(data[0])
s = data[1]

result = user_logic(n, s)
print(result)