def smallerNumbersThanCurrent(nums):
    """
    Write your logic here.
    Parameters:
        nums (list): List of integers
    Returns:
        list: List of integers where every integer represents the count of smaller elements
    """
    
    sorted_nums = sorted(nums)
    rank = {}
    
    for i, num in enumerate(sorted_nums):
        if num not in rank:
            rank[num] = i
    
    return [rank[num] for num in nums]


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])
    nums = list(map(int, data[1:]))
    
    result = smallerNumbersThanCurrent(nums)
    
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
                            