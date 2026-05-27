def find_kth_largest(nums, k):
    """
    Write your logic here.
    Parameters:
        nums (list): List of integers
        k (int): The position of the cookie in terms of largest elements
    Returns:
        int: The value of the Kth largest element in the stream
    """

    nums.sort(reverse=True)

    return nums[k - 1]


def main():
    import sys

    input = sys.stdin.read
    data = input().strip().split()

    n = int(data[0])

    k = int(data[1])

    nums = list(map(int, data[2:]))

    result = find_kth_largest(nums, k)

    print(result)


if __name__ == "__main__":
    main()
                      