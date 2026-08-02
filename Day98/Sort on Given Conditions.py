def diagonal_sort(mat):
    """
    Write your logic here to sort the matrix diagonally.
    Parameters:
        mat (list of list of int): The matrix to be sorted
    Returns:
        list of list of int: The diagonally sorted matrix
    """
    m = len(mat)
    n = len(mat[0])

    def sort_diag(r, c):
        vals = []
        i, j = r, c
        while i < m and j < n:
            vals.append(mat[i][j])
            i += 1
            j += 1

        vals.sort()

        i, j = r, c
        k = 0
        while i < m and j < n:
            mat[i][j] = vals[k]
            k += 1
            i += 1
            j += 1

    for j in range(n):
        sort_diag(0, j)

    for i in range(1, m):
        sort_diag(i, 0)

    return mat


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    m = int(data[0])
    n = int(data[1])

    mat = []
    index = 2
    for i in range(m):
        row = list(map(int, data[index:index + n]))
        mat.append(row)
        index += n

    sorted_mat = diagonal_sort(mat)

    for row in sorted_mat:
        print(' '.join(map(str, row)))

if __name__ == "__main__":
    main()