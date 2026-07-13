def user_logic(n, arr):
    called = [False] * (n + 1)

    for i in range(1, n + 1):
        if not called[i]:
            called[arr[i - 1]] = True

    result = []
    for i in range(1, n + 1):
        if not called[i]:
            result.append(i)

    return result


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    n = int(data[0])
    arr = list(map(int, data[1:]))

    result = user_logic(n, arr)
    print(*result)


if __name__ == "__main__":
    main()