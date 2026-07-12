def user_logic(n, k, x, speeds):
    speeds.sort()

    count = 0
    j = 0

    for i in range(n):
        while j < n and speeds[j] - speeds[i] < k:
            j += 1
        if j < n:
            count += (n - j)
            if count > x:
                return "YES"

    return "NO"


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    n = int(data[0])
    k = int(data[1])
    x = int(data[2])
    speeds = list(map(int, data[3:]))

    result = user_logic(n, k, x, speeds)
    print(result)


if __name__ == "__main__":
    main()