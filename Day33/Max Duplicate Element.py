def find_majority_element(arr):
    """
    Write your logic here.
    Parameters:
        arr (list): List of integers
    Returns:
        int: The majority element in the array
    """
    pass

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # The first input is the integer N
    arr = list(map(int, data[1:]))  # The remaining input is the array of integers
    
    # Call user logic function and print the output
    result = find_majority_element(arr)
    print(result)

if __name__ == "__main__":
    main()