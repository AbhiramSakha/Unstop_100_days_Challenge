def check_sequence_termination(n):
    """
    Write your logic here.
    Parameters:
        n (int): The integer to check the sequence termination
    Returns:
        str: "YES" if the sequence terminates, otherwise "NO"
    """
    seen = set()

    while n != 1:
        if n in seen:
            return "NO"
        seen.add(n)

        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 3

    return "YES"


def main():
    import sys
    input = sys.stdin.read
    data = input().strip()

    n = int(data)

    result = check_sequence_termination(n)
    print(result)

if __name__ == "__main__":
    main()