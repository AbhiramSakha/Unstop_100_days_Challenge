def nCr(n, r):
    if r > n:
        return 0
    r = min(r, n - r)
    ans = 1
    for i in range(1, r + 1):
        ans = ans * (n - r + i) // i
    return ans

def user_logic(x, y):
    if x % 2 or y % 2:
        return 0

    a = x // 2
    b = y // 2

    return nCr(a + b, a)

def main():
    import sys
    data = list(map(int, sys.stdin.read().split()))
    x, y = data[0], data[1]
    print(user_logic(x, y))

if __name__ == "__main__":
    main()