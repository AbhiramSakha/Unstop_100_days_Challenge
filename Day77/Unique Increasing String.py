def count_increasing_substrings(n, s):
    unique = set()

    for i in range(n):
        unique.add(s[i])  # single character

        for j in range(i + 1, n):
            if s[j - 1] < s[j]:
                unique.add(s[i:j + 1])
            else:
                break

    return len(unique)


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    n = int(data[0])
    s = data[1]

    print(count_increasing_substrings(n, s))


if __name__ == "__main__":
    main()