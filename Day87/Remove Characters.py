def remove_characters(s):
    freq = [0] * 26

    for ch in s:
        freq[ord(ch) - ord('a')] += 1

    remove = [False] * 26
    for i in range(26):
        if freq[i] > 0 and freq[i] % (i + 1) == 0:
            remove[i] = True

    ans = []
    for ch in s:
        if not remove[ord(ch) - ord('a')]:
            ans.append(ch)

    return "".join(ans)


def main():
    import sys
    input = sys.stdin.read
    s = input().strip()

    result = remove_characters(s)
    print result


if __name__ == "__main__":
    main()