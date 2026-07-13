def user_logic(n, x, p):
    limit = min(p, 2 * n)
    total = 0

    for f in range(1, limit + 1):
        total = (total + f) % n
        if (x + total) % n == 0:
            return "Yes"

    return "No"


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    t = int(data[0])
    idx = 1
    ans = []

    for _ in range(t):
        n = int(data[idx])
        x = int(data[idx + 1])
        p = int(data[idx + 2])
        idx += 3
        ans.append(user_logic(n, x, p))

    print("\n".join(ans))


if __name__ == "__main__":
    main()