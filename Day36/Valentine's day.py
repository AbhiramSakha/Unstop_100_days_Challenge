def coin_change(coins, amount):
    """
    Write your logic here.
    Parameters:
        coins (list): List of coin denominations
        amount (int): The target amount
    Returns:
        int: Minimum number of coins needed to make up the amount, or -1 if not possible
    """
    pass

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # First input is the integer N (number of coin types)
    coins = list(map(int, data[1:n+1]))  # Next N inputs are the coin denominations
    amount = int(data[n+1])  # The last input is the amount
    
    # Call user logic function and print the output
    result = coin_change(coins, amount)
    print(result)

if __name__ == "__main__":
    main()