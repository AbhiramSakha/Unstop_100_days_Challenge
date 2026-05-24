def max_jamun(arr):
    """
    Write your logic here.
    Parameters:
        arr (list): List of integers representing the number of jamuns in each bucket
    Returns:
        int: Maximum sum of jamuns that can be obtained by picking non-adjacent buckets
    """
    
    prev2 = 0
    prev1 = 0

    for num in arr:
        curr = max(prev1, prev2 + num)
        prev2 = prev1
        prev1 = curr

    return prev1

import sys
input = sys.stdin.read
data = input().strip().split()

n = int(data[0])  # First input is the integer N
arr = list(map(int, data[1:]))  # Remaining input is the array of integers representing jamuns in each bucket

# Call user logic function and print the output
result = max_jamun(arr)
print(result)