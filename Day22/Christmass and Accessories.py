def find_possible_combinations(n, b, c, a):
    result = []

    def backtrack(path, b, c, a):
        # If required length reached
        if len(path) == n:
            result.append("".join(path))
            return

        # Try Bell
        if b > 0:
            path.append('B')
            backtrack(path, b - 1, c, a)
            path.pop()

        # Try Candy
        if c > 0:
            path.append('C')
            backtrack(path, b, c - 1, a)
            path.pop()

        # Try Balloon
        if a > 0:
            path.append('A')
            backtrack(path, b, c, a - 1)
            path.pop()

    backtrack([], b, c, a)
    return result


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # First input is the integer n
    b = int(data[1])  # Second input is the integer B
    c = int(data[2])  # Third input is the integer C
    a = int(data[3])  # Fourth input is the integer A
    
    # Call user logic function and get the result
    result = find_possible_combinations(n, b, c, a)
    
    # Print each combination in a new line
    for combination in result:
        print(combination)

if __name__ == "__main__":
    main()