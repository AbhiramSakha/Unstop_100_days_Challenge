def pudding(n):
    """
    Write your logic here.
    Parameters:
        n (str): String representation of the number
    Returns:
        bool: True for Good pudding, False for Bad pudding
    """
    return n[-1] != '0'

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    T = int(data[0])
    results = []
    
    for i in range(1, T + 1):
        n = data[i]
        results.append(pudding(n))
    
    for result in results:
        print(1 if result else 0)

if __name__ == "__main__":
    main()