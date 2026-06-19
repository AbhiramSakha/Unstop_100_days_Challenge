def canFormStrings(s, arr):
    """
    Write your logic here.
    Parameters:
        s (str): The main string S
        arr (list of str): The array of strings
    Returns:
        bool: Return true if all strings in the array can be formed using characters from S, otherwise false
    """
    chars = set(s)
    for word in arr:
        for char in word:
            if char not in chars:
                return False

    return True  # Placeholder return value

if __name__ == '__main__':
    s = input().strip()  # Read the string S
    n = int(input().strip())  # Read the size of the string array
    arr = [input().strip() for _ in range(n)]  # Read each string in the array

    # Call the user logic function and print the output
    result = canFormStrings(s, arr)
    print('true' if result else 'false')
                