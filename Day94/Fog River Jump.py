def can_frog_cross_river(nums):
    max_reach = 0

    for i in range(len(nums)):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + nums[i])

    return True

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # First input is the integer N
    nums = list(map(int, data[1:n+1]))  # Next N integers are the magical power values
    
    # Call user logic function and print the output
    result = can_frog_cross_river(nums)
    print("true" if result else "false")

if __name__ == "__main__":
    main()
