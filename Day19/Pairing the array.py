from collections import defaultdict
from math import gcd

def count_divisible_pairs(k, arr):
    gcd_count = defaultdict(int)

    for num in arr:
        g = gcd(num, k)
        gcd_count[g] += 1

    keys = list(gcd_count.keys())
    count = 0

    for i in range(len(keys)):
        g1 = keys[i]
        for j in range(i, len(keys)):
            g2 = keys[j]
            if (g1 * g2) % k == 0:
                if g1 == g2:
                    count += gcd_count[g1] * (gcd_count[g1] - 1) // 2
                else:
                    count += gcd_count[g1] * gcd_count[g2]
    
    return count

k = int(input())
n = int(input())
arr = list(map(int, input().split()))
print(count_divisible_pairs(k, arr))