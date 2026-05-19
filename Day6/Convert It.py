# Read input
N = int(input())
arr = list(map(int, input().split()))

# Initialize max_so_far
max_so_far = 0

# Modify array
for i in range(N):
    max_so_far = max(max_so_far, arr[i])
    arr[i] += max_so_far

# Print result
print(' '.join(map(str, arr)))