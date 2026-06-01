def word_break(s, word_dict):
    word_set = set(word_dict)
    n = len(s)

    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break

    return dp[n]


def main():
    import sys

    lines = [line.strip() for line in sys.stdin.readlines() if line.strip()]

    s = lines[0]
    n = int(lines[1])

    word_dict = lines[2:2 + n]

    print("true" if word_break(s, word_dict) else "false")


if __name__ == "__main__":
    main()