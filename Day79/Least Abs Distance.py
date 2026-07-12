def user_logic(s, ch):
    n = len(s)
    ans = [0] * n

    prev = -10**9
    for i in range(n):
        if s[i] == ch:
            prev = i
        ans[i] = i - prev

    prev = 10**9
    for i in range(n - 1, -1, -1):
        if s[i] == ch:
            prev = i
        ans[i] = min(ans[i], prev - i)

    return ans


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')

    s = data[0]
    ch = data[1]

    result = user_logic(s, ch)
    print(' '.join(map(str, result)))


if __name__ == "__main__":
    main()