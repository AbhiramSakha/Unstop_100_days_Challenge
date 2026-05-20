def validate_stack_sequences(pushed, popped):
    """
    Write your logic here.
    Parameters:
        pushed (list): List of integers representing the pushed sequence
        popped (list): List of integers representing the popped sequence
    Returns:
        tuple: (bool, int) where the first element is True if the popped sequence is valid, else False,
               and the second element is the count of prime numbers if the sequence is invalid
    """
    pass

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # First input is the integer n
    pushed = list(map(int, data[1:n+1]))  # Next n integers are the pushed sequence
    popped = list(map(int, data[n+1:2*n+1]))  # Next n integers are the popped sequence
    
    # Call user logic function
    is_valid, prime_count = validate_stack_sequences(pushed, popped)
    
    # Print the output based on the returned values
    if is_valid:
        print("true")
    else:
        print("false")
        print(prime_count)

if __name__ == "__main__":
    main()