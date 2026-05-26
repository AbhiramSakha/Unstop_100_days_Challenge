def rearrange_blocks_to_form_name(S, P):
    """
    Write your logic here.
    Parameters:
        S (str): The string made by arranging the N blocks in a line
        P (str): The baby's name
    Returns:
        Tuple[int, List[int]]: Number of groups of blocks that can form the baby's name and the list of starting indices
    """
    pass

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    
    S = data[0]  # First line is the string S
    P = data[1]  # Second line is the string P
    
    # Call user logic function and get the result
    num_groups, indices = rearrange_blocks_to_form_name(S, P)
    
    # Print the output as specified
    print(num_groups)
    if num_groups == 0:
        print("none")
    else:
        print(" ".join(map(str, indices)))

if __name__ == "__main__":
    main()