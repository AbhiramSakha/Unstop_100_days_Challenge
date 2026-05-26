def find_snoop_day_index(n, arr):
    total = sum(arr)
    curr = 0

    for i in range(n):
        curr += arr[i]

        if curr * 2 >= total:
            return i + 1   # 1-based index


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    n = int(data[0])
    arr = list(map(int, data[1:]))

    result = find_snoop_day_index(n, arr)
    print(result)

if __name__ == "__main__":
    main()
                          