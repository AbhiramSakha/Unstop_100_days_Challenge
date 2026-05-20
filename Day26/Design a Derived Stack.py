def user_logic(capacity, operations):
    """
    Write your logic here.
    Parameters:
        capacity (int): Maximum capacity of the stack
        operations (list of str): List of operations to be performed on the stack
    Returns:
        list of str: Result of each operation according to the problem statement
    """
    pass


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    
    capacity = int(data[0])  # First line is the capacity of the stack
    num_operations = int(data[1])  # Second line is the number of operations
    operations = data[2:]  # Remaining lines are the operations

    # Call user logic function and get the results
    results = user_logic(capacity, operations)
    
    # Print each result in the required format
    for result in results:
        print(result)

if __name__ == "__main__":
    main()