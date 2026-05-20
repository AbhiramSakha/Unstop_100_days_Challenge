def user_logic(n, a, b):
    """
    Write your logic here.
    Parameters:
        n (int): Number of elements in the arrays
        a (list): List of integers representing the first array
        b (list): List of integers representing the second array
    Returns:
        int: Computed passcode to unlock the locker
    """
    pass

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # First input is the integer N
    a = list(map(int, data[1:n+1]))  # Next N inputs are the elements of the first array
    b = list(map(int, data[n+1:2*n+1]))  # Next N inputs are the elements of the second array
    
    # Call user logic function and print the output
    result = user_logic(n, a, b)
    print(result)

if __name__ == "__main__":
    main()