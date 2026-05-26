def change_longest(arr, x):
    mx = max(arr)

    for i in range(len(arr)):
        if arr[i] == mx:
            arr[i] = max(0, arr[i] - x)


def pole_arrangement(arr):
    n = len(arr)

    if n < 3:
        return False

    left_min = [0] * n
    left_min[0] = arr[0]

    for i in range(1, n):
        left_min[i] = min(left_min[i - 1], arr[i])

    stack = []

    for j in range(n - 1, -1, -1):
        while stack and stack[-1] <= left_min[j]:
            stack.pop()

        if stack and stack[-1] < arr[j]:
            return True

        stack.append(arr[j])

    return False


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    n = int(data[0])
    x = int(data[1])

    arr = list(map(int, data[2:2 + n]))

    change_longest(arr, x)

    print(1 if pole_arrangement(arr) else 0)


if __name__ == "__main__":
    main()
