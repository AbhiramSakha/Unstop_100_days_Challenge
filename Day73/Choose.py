def user_logic(n, k, a, b):
    """
    Write your logic here.
    Parameters:
        n (int): The number of elements in sequences A and B
        k (int): The integer K
        a (list): List of integers representing sequence A
        b (list): List of integers representing sequence B
    Returns:
        str: "Yes" if conditions are satisfied, otherwise "No"
    """
    canA = True
    canB = True

    for i in range(1, n):
        newA = (canA and abs(a[i - 1] - a[i]) <= k) or \
               (canB and abs(b[i - 1] - a[i]) <= k)

        newB = (canA and abs(a[i - 1] - b[i]) <= k) or \
               (canB and abs(b[i - 1] - b[i]) <= k)

        canA, canB = newA, newB

    return "Yes" if (canA or canB) else "No"


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    n = int(data[0])
    k = int(data[1])
    a = list(map(int, data[2:n + 2]))
    b = list(map(int, data[n + 2:2 * n + 2]))

    result = user_logic(n, k, a, b)
    print(result)


if __name__ == "__main__":
    main()