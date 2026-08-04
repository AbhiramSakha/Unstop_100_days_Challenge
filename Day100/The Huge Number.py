def user_logic(n):
    """
    Write your logic here.
    Parameters:
        n (int): An integer N
    Returns:
        int: The maximum hugeness that is a Huge Number as well, or -1 if there is no Huge Number
    """

    # Maximum hugeness after considering numbers till n
    max_hugeness = (1 << (n.bit_length())) - 1

    # Mersenne primes within range for n <= 1e9
    mersenne_primes = [
        3,
        7,
        31,
        127,
        8191,
        131071,
        524287,
        2147483647
    ]

    ans = -1

    for p in mersenne_primes:
        if p <= max_hugeness:
            ans = p

    return ans


def main():
    import sys
    input = sys.stdin.read
    data = input().strip()

    n = int(data)

    result = user_logic(n)
    print(result)

if __name__ == "__main__":
    main()