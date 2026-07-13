def check_word_beauty(word):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    count = 0

    for ch in word:
        if ch in vowels:
            count += 1

    if count % 2 == 0:
        return "WORD IS BEAUTIFUL"
    else:
        return "WORD IS UGLY"


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    T = int(data[0])
    words = data[1:]

    results = []
    for word in words:
        results.append(check_word_beauty(word))

    print("\n".join(results))


if __name__ == "__main__":
    main()