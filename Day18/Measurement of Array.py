def user_logic(n, arr):
    """
    Write your logic here.
    Parameters:
        n (int): Number of elements in the array
        arr (list of int): List of integers
    Returns:
        int: Computed result based on the problem statement
    """
    pass

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # First input is the integer n
    arr = list(map(int, data[1:]))  # Remaining input is the array of integers
    
    # Call user logic function and print the output
    result = user_logic(n, arr)
    print(result)

if __name__ == "__main__":
    main()