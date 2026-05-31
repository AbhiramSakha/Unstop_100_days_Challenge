def prime_matrix(n, matrix):
    def is_prime(num):
        if num < 2:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False

        i = 3
        while i * i <= num:
            if num % i == 0:
                return False
            i += 2

        return True

    rows = set()
    cols = set()

    # Find all rows and columns containing prime numbers
    for i in range(n):
        for j in range(n):
            if is_prime(matrix[i][j]):
                rows.add(i)
                cols.add(j)

    # Mark corresponding rows and columns as -1
    for i in range(n):
        for j in range(n):
            if i in rows or j in cols:
                matrix[i][j] = -1

    return matrix


def main():
    import sys
    input_data = sys.stdin.read().strip().split()

    n = int(input_data[0])

    matrix = []
    idx = 1
    for i in range(n):
        row = []
        for j in range(n):
            row.append(int(input_data[idx]))
            idx += 1
        matrix.append(row)

    modified_matrix = prime_matrix(n, matrix)

    for row in modified_matrix:
        print(*row)


if __name__ == "__main__":
    main()