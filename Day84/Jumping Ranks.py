def solve(arr):
    """
    Write your logic here.
    Parameters:
        arr (list): List of integers
    Returns:
        list: List of integers representing the number of ranks between the student's initial and final level
    """
    first = {}
    last = {}

    for i, x in enumerate(arr):
        if x not in first:
            first[x] = i
        last[x] = i

    result = []
    for x in arr:
        result.append(last[x] - first[x])

    return result


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    n = int(data[0])
    arr = list(map(int, data[1:n + 1]))

    result = solve(arr)

    print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()