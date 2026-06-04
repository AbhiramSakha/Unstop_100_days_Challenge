def user_logic(n):
    """
    Write your logic here.
    Parameters:
        n (int): integer representing the number of stones
    Returns:
        bool: True if Bolt wins the game, otherwise False
    """
    dp = [False] * (n + 1)

    for i in range(1, n + 1):
        j = 1
        while j * j <= i:
            if not dp[i - j * j]:
                dp[i] = True
                break
            j += 1

    return dp[n]


def main():
    import sys
    input = sys.stdin.read
    data = input().strip()

    n = int(data)

    result = user_logic(n)
    print("True" if result else "False")


if __name__ == "__main__":
    main()