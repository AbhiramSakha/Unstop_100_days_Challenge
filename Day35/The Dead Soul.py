def find_minimum_k(a, b, c):
    d = 4 * a * c

    def valid(k):
        return (b - k) * (b - k) >= d

    k = 0
    while True:
        if valid(k) or valid(-k):
            return k
        k += 1


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    T = int(data[0])
    index = 1
    results = []

    for _ in range(T):
        a = int(data[index])
        b = int(data[index + 1])
        c = int(data[index + 2])
        index += 3

        result = find_minimum_k(a, b, c)
        results.append(result)

    for result in results:
        print(result)


if __name__ == "__main__":
    main()
                            