def can_convert_to_zero(s):
    a, b, c = map(int, s.split('-'))

    total = a + b + c

    if total % 2 != 0:
        return "NO"

    if a + b < c or a + c < b or b + c < a:
        return "NO"

    return "YES"


def main():
    import sys
    input = sys.stdin.read

    s = input().strip()
    print(can_convert_to_zero(s))


if __name__ == "__main__":
    main()