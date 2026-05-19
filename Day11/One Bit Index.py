def is_power_of_two(x):
    return x > 0 and (x & (x - 1)) == 0

def count_good_indices(arr):
    count = 0
    prefix_sum = 0
    for num in arr:
        prefix_sum += num
        if is_power_of_two(prefix_sum):
            count += 1
    return count

# Input
n = int(input())
arr = list(map(int, input().split()))

# Output
print(count_good_indices(arr))
                  