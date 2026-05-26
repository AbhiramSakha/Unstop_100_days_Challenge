def is_happy_number(n):
    """
    Write your logic here.
    Parameters:
        n (int): The starting number
    Returns:
        bool: True if n is a happy number, False otherwise
    """
    pass


def main():
    import sys
    input = sys.stdin.read

    # Read input
    data = input().strip()
    n = int(data)

    # Call user logic function and print the output
    result = is_happy_number(n)
    print("true" if result else "false")


if __name__ == "__main__":
    main()
