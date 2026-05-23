def LongestConsecutiveCharacter(s):
    max_len = 1
    curr_len = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            curr_len += 1
        else:
            max_len = max(max_len, curr_len)
            curr_len = 1

    max_len = max(max_len, curr_len)
    return max_len


def main():
    import sys
    input = sys.stdin.read
    s = input().strip()

    result = LongestConsecutiveCharacter(s)
    print(result)

if __name__ == "__main__":
    main()