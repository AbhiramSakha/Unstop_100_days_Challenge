def num_of_pairs(nums, target):
    count = 0
    n = len(nums)

    for i in range(n):
        for j in range(n):
            if i != j and nums[i] + nums[j] == target:
                count += 1

    return count

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # First input is the integer n
    arr = data[1:n+1]  # Next n inputs are the elements of the array
    target = data[n+1]  # The last input is the target string
    
    # Call user logic function and print the output
    result = num_of_pairs(arr, target)
    print(result)

if __name__ == "__main__":
    main()