def calculate_sum(nums):
    """
    Logic to find the smallest missing positive integer,
    then add ASCII value of its first digit to the sum of the array.
    """
    n = len(nums)

    # Step 1: Rearrange numbers to their correct index positions
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            correct_idx = nums[i] - 1
            nums[i], nums[correct_idx] = nums[correct_idx], nums[i]

    # Step 2: Find the first index i where nums[i] != i + 1
    missing = n + 1
    for i in range(n):
        if nums[i] != i + 1:
            missing = i + 1
            break

    # Step 3: ASCII of first digit of missing number
    first_digit_ascii = ord(str(missing)[0])

    # Step 4: Final result = sum of nums + ASCII value
    return sum(nums) + first_digit_ascii

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    n = int(data[0])  # First input is the integer N
    nums = list(map(int, data[1:]))  # Remaining input is the array of integers

    result = calculate_sum(nums)
    print(result)

if __name__ == "__main__":
    main()