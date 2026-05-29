def special_series(A, B, N):
    """
    Write your logic here.
    Parameters:
        A (int): First integer
        B (int): Second integer
        N (int): Term to find in the special series
    Returns:
        int: The Nth term of the special series
    """
    if N == 1:
        return A
    elif N == 2:
        return B
    
    # Initialize the first two terms
    term1 = A
    term2 = B
    
    # Calculate terms from 3 to N
    for _ in range(3, N + 1):
        next_term = abs(term2 - term1)
        term1 = term2
        term2 = next_term
    
    return term2

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    A = int(data[0])
    B = int(data[1])
    N = int(data[2])
    
    # Call user logic function and print the output
    result = special_series(A, B, N)
    print(result)

if __name__ == "__main__":
    main()