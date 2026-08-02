def count_square_sub_islands(matrix):
    """
    Write your logic here.
    Parameters:
        matrix (list of list of int): 2D list representing the matrix
    Returns:
        int: Count of square sub-islands
    """
    if not matrix:
        return 0

    n = len(matrix)
    m = len(matrix[0])

    dp = [[0] * m for _ in range(n)]
    total = 0

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],
                        dp[i][j - 1],
                        dp[i - 1][j - 1]
                    )
                total += dp[i][j]

    return total


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    n = int(data[0])
    m = int(data[1])

    matrix = []
    index = 2
    for i in range(n):
        row = list(map(int, data[index:index + m]))
        matrix.append(row)
        index += m

    result = count_square_sub_islands(matrix)
    print(result)


if __name__ == "__main__":
    main()