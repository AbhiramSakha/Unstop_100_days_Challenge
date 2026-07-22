def pancake_sort(arr):
    res = []
    n = len(arr)

    for curr in range(n, 1, -1):
        idx = arr.index(curr)

        if idx == curr - 1:
            continue

        if idx != 0:
            res.append(idx + 1)
            arr[:idx + 1] = arr[:idx + 1][::-1]

        res.append(curr)
        arr[:curr] = arr[:curr][::-1]

    return res


def main():
    import sys
    data = list(map(int, sys.stdin.read().split()))

    n = data[0]
    arr = data[1:]

    ans = pancake_sort(arr)

    if ans:
        print(' '.join(map(str, ans)))
    else:
        print()


if __name__ == "__main__":
    main()