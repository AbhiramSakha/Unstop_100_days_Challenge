def reverse_parentheses(s):
    n = len(s)
    pair = [0] * n
    stack = []

    for i, ch in enumerate(s):
        if ch == '(':
            stack.append(i)
        elif ch == ')':
            j = stack.pop()
            pair[i] = j
            pair[j] = i

    res = []
    i = 0
    d = 1

    while i < n:
        if s[i] == '(' or s[i] == ')':
            i = pair[i]
            d = -d
        else:
            res.append(s[i])
        i += d

    return ''.join(res)

def main():
    import sys
    s = sys.stdin.read().strip()
    print(reverse_parentheses(s))

if __name__ == "__main__":
    main()