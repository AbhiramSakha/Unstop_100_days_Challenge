def find_anagram_indices(secret1, secret2):
    """
    Write your logic here.
    Parameters:
        secret1 (str): The first string representing Secret 1
        secret2 (str): The second string representing Secret 2
    Returns:
        list: List of starting indices of substrings in Secret 1 that are anagrams of Secret 2
    """
    pass


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    secret1 = data[0]  # First line input representing Secret 1
    secret2 = data[1]  # Second line input representing Secret 2
    
    # Call user logic function and get the result
    result = find_anagram_indices(secret1, secret2)
    
    if not result:
        print("Empty Array")
    else:
        print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()