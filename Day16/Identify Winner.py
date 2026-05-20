from collections import Counter

def find_winner(nums):
    freq = Counter(nums)  # Count frequencies of all numbers
    for num in nums:
        if freq[num] == 1:
            return num  # First number with frequency 1
    return 0  # No unique number found

if __name__ == '__main__':
    N = int(input())
    nums = list(map(int, input().split()))
    print(find_winner(nums))