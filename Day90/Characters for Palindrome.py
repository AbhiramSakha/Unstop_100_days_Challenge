def user_logic(n, s):
    freq = [0] * 26
    for ch in s:
        freq[ord(ch) - ord('a')] += 1

    odd_chars = []
    for i in range(26):
        if freq[i] % 2 == 1:
            odd_chars.append(chr(i + ord('a')))

    if len(odd_chars) <= 1:
        return "-1"

    # Add one occurrence of all but one odd-frequency character.
    return "".join(odd_chars[:-1])


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    n = int(data[0])
    s = data[1]

    print(user_logic(n, s))


if __name__ == "__main__":
    main()