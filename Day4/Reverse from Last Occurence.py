def transform_string(s, ch):
    """
    Reverses the portion of the string from the last occurrence of ch to the end.
    
    Parameters:
        s (str): Input string.
        ch (str): Character to be used in transformation.
    
    Returns:
        str: Transformed string.
    """
    last_index = s.rfind(ch)
    
    if last_index == -1:
        return s  # Character not found
    
    # Reverse substring from last_index to end
    return s[:last_index] + s[last_index:][::-1]

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    s = data[0]  # First input is the string s
    ch = data[1]  # Second input is the character ch
    
    # Call user logic function and print the output
    transformed_string = transform_string(s, ch)
    print(transformed_string)

if __name__ == "__main__":
    main()