from math import gcd

def solve(x, y):
    days = 0

    while x > 0 and y > 0:
        g = gcd(x, y)
        x -= g
        y -= g
        days += 1

    return days


def main():
    import sys
    data = list(map(int, sys.stdin.read().split()))
    x, y = data
    print(solve(x, y))


if __name__ == "__main__":
    main()