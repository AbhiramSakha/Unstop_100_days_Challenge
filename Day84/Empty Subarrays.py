def count_empty_subarrays(arr):
    """
    Write your logic here.
    Parameters:
        arr (list): List of integers
    Returns:
        int: Number of empty subarrays present in the given array
    """
    prefix_sum = 0
    freq = {0: 1}
    count = 0

    for num in arr:
        prefix_sum += num
        if prefix_sum in freq:
            count += freq[prefix_sum]
            freq[prefix_sum] += 1
        else:
            freq[prefix_sum] = 1

    return count


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    n = int(data[0])
    arr = list(map(int, data[1:n + 1]))

    result = count_empty_subarrays(arr)
    print(result)


if __name__ == "__main__":
    main()