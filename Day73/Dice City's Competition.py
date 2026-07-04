def user_logic(n, s):
    """
    Write your logic here.
    Parameters:
        n (int): Length of the string s
        s (str): A string of length n consisting of lowercase letters only
    Returns:
        int: Number of distinct strings that can be formed by removing two consecutive letters
    """
    seen = set()

    for i in range(n - 1):
        seen.add(s[:i] + s[i + 2:])

    return len(seen)


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    T = int(data[0])
    index = 1
    results = []

    for _ in range(T):
        n = int(data[index])
        s = data[index + 1]
        index += 2
        results.append(user_logic(n, s))

    print(*results, sep="\n")


if __name__ == "__main__":
    main()