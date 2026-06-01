def get_treasure(n):
    if n <= 2:
        return n

    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b

    return b


def main():
    import sys
    input = sys.stdin.read
    data = input().strip()

    n = int(data)

    result = get_treasure(n)
    print(result)


if __name__ == "__main__":
    main()