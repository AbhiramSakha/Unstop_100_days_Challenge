def user_logic(t, test_cases):
    results = []

    for s in test_cases:
        # Generate marked binary string
        marked = [s[0]]
        for i in range(1, len(s)):
            if s[i] != marked[-1]:
                marked.append('1')
            else:
                marked.append('0')

        marked_str = "".join(marked)

        # If marked binary is same as input, print -1
        if marked_str == s:
            results.append(-1)
        else:
            results.append(int(marked_str, 2))

    return results


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    t = int(data[0])
    test_cases = data[1:t + 1]

    results = user_logic(t, test_cases)

    for result in results:
        print(result)


if __name__ == "__main__":
    main()