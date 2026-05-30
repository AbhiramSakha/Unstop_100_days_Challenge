def execute_instructions(n, pos, instruction):
    m = len(instruction)
    ans = []

    for i in range(m):
        r, c = pos
        count = 0

        for j in range(i, m):
            ch = instruction[j]

            if ch == 'L':
                c -= 1
            elif ch == 'R':
                c += 1
            elif ch == 'U':
                r -= 1
            else:
                r += 1

            if r < 0 or r >= n or c < 0 or c >= n:
                break

            count += 1

        ans.append(count)

    return ans


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    n = int(data[0])

    pos = [int(data[1]), int(data[2])]

    m = int(data[3])
    instruction = data[4]

    result = execute_instructions(n, pos, instruction)

    print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()