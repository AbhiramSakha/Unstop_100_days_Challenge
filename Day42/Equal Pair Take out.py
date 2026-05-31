def user_logic(n, id_vector, size_vector):
    stack = []

    for i in range(n):
        current = (id_vector[i], size_vector[i])

        if stack and stack[-1] == current:
            stack.pop()
        else:
            stack.append(current)

    return len(stack)


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])

    id_vector = list(map(int, data[1:n + 1]))
    size_vector = list(map(int, data[n + 1:2 * n + 1]))

    result = user_logic(n, id_vector, size_vector)
    print(result)

if __name__ == "__main__":
    main()