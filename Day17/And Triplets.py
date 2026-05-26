from collections import defaultdict

def count_and_triplets(arr):
    freq = defaultdict(int)

    for a in arr:
        for b in arr:
            freq[a & b] += 1

    count = 0
    for c in arr:
        for val, f in freq.items():
            if (val & c) == 0:
                count += f

    return count

n = int(input())
arr = list(map(int, input().split()))
print(count_and_triplets(arr))