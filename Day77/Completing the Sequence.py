def add_minimum_changes(word):
    pattern = "pqr"
    expected = 0
    insertions = 0

    for ch in word:
        while pattern[expected] != ch:
            insertions += 1
            expected = (expected + 1) % 3
        expected = (expected + 1) % 3

    if expected != 0:
        insertions += 3 - expected

    return insertions


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    n = int(data[0])
    word = data[1]

    print(add_minimum_changes(word))


if __name__ == "__main__":
    main()