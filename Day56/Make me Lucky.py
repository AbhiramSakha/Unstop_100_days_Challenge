def make_me_lucky(S, U):
    m = len(U)
    stack = []

    for ch in S:
        stack.append(ch)
        if len(stack) >= m and ''.join(stack[-m:]) == U:
            del stack[-m:]

    return ''.join(stack)

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    S = data[0]
    U = data[1]

    result = make_me_lucky(S, U)
    print(result)

if __name__ == "__main__":
    main()