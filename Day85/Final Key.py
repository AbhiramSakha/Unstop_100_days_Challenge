def first_uniq_char(s):
    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    for i, ch in enumerate(s):
        if freq[ch] == 1:
            return i

    return -1


def main():
    import sys
    input = sys.stdin.read
    s = input().strip()

    index = first_uniq_char(s)
    if index == -1:
        print(-1)
    else:
        print(index)


if __name__ == "__main__":
    main()