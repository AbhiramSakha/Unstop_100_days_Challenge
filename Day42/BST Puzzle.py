MOD = 10**9 + 7

import sys

data = list(map(int, sys.stdin.read().strip().split()))

values = [x for x in data if x != -1]

values.sort()

ans = 0
for i, v in enumerate(values):
    ans = (ans + v * (i + 1)) % MOD

print(ans)