def minOperations(n):
    return (n * n) // 4


def main():
    import sys
    input = sys.stdin.read
    n = int(input().strip())

    result = minOperations(n)
    print(result)


if __name__ == "__main__":
    main()