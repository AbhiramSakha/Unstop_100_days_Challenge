def determine_color(s):
    """
    Determines the color of the chessboard cell.
    
    Parameters:
        s (str): Input string representing a position (e.g., 'a1', 'b2').
        
    Returns:
        str: "Black" or "White" based on the cell's color.
    """
    # Convert column (a-h) to number 1-8
    column = ord(s[0].lower()) - ord('a') + 1
    row = int(s[1])
    
    # Sum determines color
    if (column + row) % 2 == 0:
        return "Black"
    else:
        return "White"

def main():
    import sys
    input = sys.stdin.read
    s = input().strip()  # Read the input string
    
    # Call the user logic function and print the output
    result = determine_color(s)
    print(result)

if __name__ == "__main__":
    main()
                            