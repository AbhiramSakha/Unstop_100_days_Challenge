from collections import Counter

def user_logic(n, arr):
    """
    Write your logic here.
    Parameters:
        n (int): Size of the array
        arr (list): List of integers representing team numbers
    Returns:
        list: List of team numbers with the maximum number of players
    """
    
    freq = Counter(arr)
    
    max_freq = max(freq.values())
    
    result = [team for team, count in freq.items() if count == max_freq]
    
    return sorted(result)


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # First input is the integer n
    arr = list(map(int, data[1:]))  # Remaining input is the array of integers
    
    # Call user logic function and get the result
    result = user_logic(n, arr)
    
    # Print each team number in the result on a new line
    for team in result:
        print(team)

if __name__ == "__main__":
    main()