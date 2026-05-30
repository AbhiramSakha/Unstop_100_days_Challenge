def user_logic(n, friends):
    ans = 0

    for k in range(n + 1):
        count = 0

        for a, b in friends:
            if a >= k - 1 - count and b >= count:
                count += 1

        if count >= k:
            ans = k

    return ans


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    index = 0
    T = int(data[index])
    index += 1

    results = []

    for _ in range(T):
        n = int(data[index])
        index += 1

        friends = []

        for _ in range(n):
            ai = int(data[index])
            bi = int(data[index + 1])
            friends.append((ai, bi))
            index += 2

        result = user_logic(n, friends)
        results.append(result)

    for result in results:
        print(result)


if __name__ == "__main__":
    main()