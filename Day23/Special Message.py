def specialmsg(s, vocab):
    """
    Write your logic here.
    Parameters:
        s (str): Input string with acronyms
        vocab (list): List of key-value pairs, each a list of two strings [key, value]
    Returns:
        str: Modified string with acronyms replaced, or '?' if acronym not found
    """
    pass

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    
    s = data[0]  # First line is the string S
    n = int(data[1])  # Second line is the size of key-value pairs
    
    vocab = []
    for i in range(2, 2 + n):
        key, value = data[i].split()
        vocab.append([key, value])
    
    # Call user logic function and print the output
    result = specialmsg(s, vocab)
    print(result)

if __name__ == "__main__":
    main()