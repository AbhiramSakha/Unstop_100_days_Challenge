#!/usr/bin/env python3
import sys

def longest_tribonacci_subarray(n, arr):
    """
    Write your logic here.
    Parameters:
        n (int): Size of the array
        arr (list): List of integers representing the array
    Returns:
        int: Length of the longest Tribonacci subarray
    """

    MAX_VAL = 100000

    # Generate Tribonacci numbers up to MAX_VAL
    trib_set = set()
    
    a, b, c = 0, 1, 1
    trib_set.add(a)
    trib_set.add(b)
    trib_set.add(c)

    while True:
        nxt = a + b + c
        if nxt > MAX_VAL:
            break
        trib_set.add(nxt)
        a, b, c = b, c, nxt

    # Find longest contiguous subarray
    max_len = 0
    curr_len = 0

    for num in arr:
        if num in trib_set:
            curr_len += 1
            max_len = max(max_len, curr_len)
        else:
            curr_len = 0

    return max_len


def main():
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # First input is the integer N
    arr = list(map(int, data[1:n+1]))  # Next N inputs are the array elements
    
    # Call user logic function and print the output
    result = longest_tribonacci_subarray(n, arr)
    print(result)

if __name__ == "__main__":
    main()