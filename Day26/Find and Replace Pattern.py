def find_and_replace_pattern(words, pattern):
    """
    Write your logic here.
    Parameters:
        words (list): List of strings representing words in the book
        pattern (str): The pattern string to match
    Returns:
        tuple: A tuple containing:
            - int: Number of words matched with the pattern
            - list: List of matched words
    """
    pass

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # First input is the integer N
    words = data[1:n+1]  # Next N inputs are the words
    pattern = data[n+1]  # The last input is the pattern string
    
    # Call user logic function
    matched_count, matched_words = find_and_replace_pattern(words, pattern)
    
    # Print the results
    print(matched_count)
    if matched_count > 0:
        print(" ".join(matched_words))

if __name__ == "__main__":
    main()