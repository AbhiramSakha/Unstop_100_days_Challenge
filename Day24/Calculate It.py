def count_expressible_numbers(X, Y):
    """
    Write your logic here.
    Parameters:
        X (int): The lower bound integer
        Y (int): The upper bound integer
    Returns:
        int: Number of integers between X and Y (inclusive) that can be expressed in the form of 2^A * 3^B
    """
    pass

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    X = int(data[0])
    Y = int(data[1])
    
    # Call user logic function and print the output
    result = count_expressible_numbers(X, Y)
    print(result)

if __name__ == "__main__":
    main()