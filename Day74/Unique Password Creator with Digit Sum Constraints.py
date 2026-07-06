def count_passwords(n):
    """
    Write your logic here.
    Parameters:
        n (int): The target sum for the password
    Returns:
        int: Number of unique passwords satisfying the given constraints
    """
    if n == 1:
        return 1
    if n == 2:
        return 2

    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b

def main():
    import sys
    input = sys.stdin.read
    n = int(input().strip())

    result = count_passwords(n)
    print(result)

if __name__ == "__main__":
    main()