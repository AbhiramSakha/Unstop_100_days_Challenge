def find_good_numbers(n):
    """
    Write your logic here.
    Parameters:
        n (int): The upper limit of the range
    Returns:
        list: List of "good" numbers from 0 to n
    """
    result = []

    for num in range(n + 1):
        s = str(num)
        good = True
        for i in range(len(s) - 1):
            if abs(int(s[i]) - int(s[i + 1])) != 1:
                good = False
                break
        if good:
            result.append(num)

    return result


def main():
    import sys
    input = sys.stdin.read
    data = input().strip()

    n = int(data)

    result = find_good_numbers(n)
    print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()