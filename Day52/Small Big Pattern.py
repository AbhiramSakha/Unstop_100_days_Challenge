def big_small_sequence(arr, n):
    if n == 0:
        return 0

    up = 1
    down = 1

    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            up = down + 1
        elif arr[i] < arr[i - 1]:
            down = up + 1

    return max(up, down)

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    n = int(data[0])
    arr = list(map(int, data[1:]))

    result = big_small_sequence(arr, n)
    print(result)

if __name__ == "__main__":
    main()