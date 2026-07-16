def solve(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for ch in s:
        if ch in "({[":
            stack.append(ch)
        else:
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()

    return len(stack) == 0


def main():
    import sys
    input = sys.stdin.read
    s = input().strip()

    result = solve(s)
    if result:
        print("True")
    else:
        print("False")


if __name__ == "__main__":
    main()