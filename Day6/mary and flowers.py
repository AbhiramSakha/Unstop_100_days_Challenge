def find_flower_indices(n, t, arr):
    """
    Finds the first pair of indices (i, j) such that arr[i] + arr[j] == t and i < j.
    Parameters:
        n (int): Total types of flowers
        t (int): Total number of flowers needed
        arr (list): List of integers representing the flowers
    Returns:
        tuple: A tuple containing two integers representing the indices of the flowers
    """
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == t:
                return (i, j)
    return (-1, -1)  # This line should never be reached based on constraints

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # First input is the integer n
    t = int(data[1])  # Second input is the integer t
    arr = list(map(int, data[2:]))  # Remaining input is the array of integers
    
    # Call user logic function and get the result
    result = find_flower_indices(n, t, arr)
    
    # Print the result
    print(result[0], result[1])

if __name__ == "__main__":
    main()