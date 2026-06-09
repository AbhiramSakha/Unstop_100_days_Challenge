def cycle_end(n, k):
    ans = 0
    for i in range(2, n + 1):
        ans = (ans + k) % i
    return ans


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    t = int(data[0])
    index = 1
    results = []

    for _ in range(t):
        n = int(data[index])
        k = int(data[index + 1])
        index += 2
        results.append(cycle_end(n, k))

    print(*results, sep="\n")


if __name__ == "__main__":
    main()