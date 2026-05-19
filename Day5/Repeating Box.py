from collections import Counter

# Read input
n = int(input())
x = list(map(int, input().split()))

# Count frequencies using Counter
freq = Counter(x)

# Find the max frequency
max_freq = max(freq.values())

# Get all numbers with that max frequency
most_common = [num for num, count in freq.items() if count == max_freq]

# Print the smallest one among them
print(min(most_common))
                            