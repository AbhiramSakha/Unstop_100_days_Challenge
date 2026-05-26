# Enter your code here. Read input from STDIN. Print output to STDOUT
def max_pair_min_sum(nums):
    nums.sort()
    # Sum of elements at even indices
    return sum(nums[i] for i in range(0, len(nums), 2))

if __name__ == "__main__":
    m = int(input().strip())          # 2N
    nums = list(map(int, input().split()))
    print(max_pair_min_sum(nums))