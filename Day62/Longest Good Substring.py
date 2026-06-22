def user_logic(s):
    n = len(s)

    if n == 1:
        return 1

    max_len = 1
    curr = 1

    for i in range(1, n):
        if ord(s[i]) - ord(s[i - 1]) == 1:
            curr += 1
        else:
            curr = 1
        max_len = max(max_len, curr)

    run = 1
    i = n - 2
    while i > 0 and ord(s[i]) - ord(s[i - 1]) == 1:
        run += 1
        i -= 1

    if s[n - 2] != 'z':
        max_len = max(max_len, run + 1)

    return max_len

def main():
    import sys
    input = sys.stdin.read
    s = input().strip()

    result = user_logic(s)
    print(result)


if __name__ == "__main__":
    main()