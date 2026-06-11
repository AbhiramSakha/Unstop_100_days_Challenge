def user_logic(str, pattern):
    """
    Write your logic here.
    Parameters:
        str (str): The input string
        pattern (str): The pattern string
    Returns:
        tuple: A tuple containing the required substring and the index
    """
    idx = str.find(pattern)

    if idx == -1:
        return (str, -1)

    return (str[:idx], idx)


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    str = data[0]
    pattern = data[1]

    result_substring, index = user_logic(str, pattern)

    print(result_substring, index)

if __name__ == "__main__":
    main()