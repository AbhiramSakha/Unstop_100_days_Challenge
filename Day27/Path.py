def user_logic(n, s):
    """
    Write your logic here.
    Parameters:
        n (int): The number of rooms in the house
        s (str): The sequence of puzzles and pieces
    Returns:
        int: The minimum number of pieces that the person needs to buy
    """
    pass


 def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    n = int(data[0])  # First input is the integer n
    s = data[1]       # Second input is the string s

    # Call user logic function and print the output
    result = user_logic(n, s)
    print(result)


 if __name__ == "__main__":
    main()