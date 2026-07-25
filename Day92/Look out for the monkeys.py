def monkeys_visible_from_each_pole(n, heights):
    res = [0] * n
    stack = []

    # Process from right to left
    for i in range(n - 1, -1, -1):
        cnt = 0

        # All shorter poles are visible
        while stack and heights[i] > stack[-1]:
            stack.pop()
            cnt += 1

        # First taller/equal pole is also visible (if any)
        if stack:
            cnt += 1

        res[i] = cnt
        stack.append(heights[i])

    return res


def main():
    import sys
    data = list(map(int, sys.stdin.read().split()))

    n = data[0]
    heights = data[1:]

    ans = monkeys_visible_from_each_pole(n, heights)
    print(*ans)


if __name__ == "__main__":
    main()