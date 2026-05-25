def max_sum_after_partitioning(arr, k):
    """
    Write your logic here.
    Parameters:
        arr (list): List of integers
        k (int): Maximum allowed size for each subarray
    Returns:
        int: Maximum sum after partitioning the array
    """
    pass

def sieve_of_eratosthenes(n):
    """
    Write your logic here.
    Parameters:
        n (int): Upper limit to find prime numbers
    Returns:
        int: Count of prime numbers less than or equal to n
    """
    pass

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # First input is the integer N (size of the array)
    arr = list(map(int, data[1:n+1]))  # Next N inputs are the array elements
    k = int(data[n+1])  # Last input is the integer K (maximum allowed size for each subarray)
    
    # Call user logic functions
    max_sum = max_sum_after_partitioning(arr, k)
    prime_count = sieve_of_eratosthenes(max_sum)
    
    # Print the result
    print(prime_count)

if __name__ == "__main__":
    main()