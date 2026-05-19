def max_difference(arr):
    min_value = arr[0]
    max_diff = -1
    
    for j in range(1, len(arr)):
        if arr[j] > min_value:
            max_diff = max(max_diff, arr[j] - min_value)
        else:
            min_value = min(min_value, arr[j])
    
    return max_diff

# Input processing
T = int(input())
results = []

for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    results.append(max_difference(arr))

# Output
for res in results:
    print(res)
                         