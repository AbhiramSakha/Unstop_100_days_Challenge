def user_logic(n, positions_cards):
    """
    Write your logic here.
    Parameters:
        n (int): Number of positions
        positions_cards (list of tuples): List of tuples where each tuple contains two integers (pi, ci)
    Returns:
        int: Maximum number of cards Lexi can collect
    """
    pass



def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    n = int(data[0])
    positions_cards = []
    index = 1
    for _ in range(n):
        pi = int(data[index])
        ci = int(data[index + 1])
        positions_cards.append((pi, ci))
        index += 2

    # Call user logic function and print the output
    result = user_logic(n, positions_cards)
    print(result)


if __name__ == "__main__":
    main()
