def find_misplaced_file(n, file_numbers):
    """
    Write your logic here.
    Parameters:
        n (int): Total number of files.
        file_numbers (list): List of integers representing the numbers on the files found after the accident.
    Returns:
        int: The number on the misplaced file.
    """
    ans = 0
    for num in file_numbers:
        ans ^= num
    return ans


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])
    file_numbers = list(map(int, data[1:]))
    
    result = find_misplaced_file(n, file_numbers)
    print(result)

if __name__ == "__main__":
    main()