def find_middle_earth(nums1, nums2):
    """
    Returns median of two arrays
    """

    arr = nums1 + nums2
    arr.sort()

    n = len(arr)

    if n % 2 == 1:
        return float(arr[n // 2])

    return (arr[n // 2 - 1] + arr[n // 2]) / 2.0


def main():
    import sys

    data = sys.stdin.read().strip().split()

    m = int(data[0])
    n = int(data[1])

    nums1 = list(map(int, data[2:2 + m]))
    nums2 = list(map(int, data[2 + m:2 + m + n]))

    result = find_middle_earth(nums1, nums2)

    print(f"{result:.1f}")


if __name__ == "__main__":
    main()
                     