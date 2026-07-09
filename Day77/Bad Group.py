from math import gcd

def find_bad(arr):
    """
    Write your logic here.
    Parameters:
        arr (list): List of integers representing the array of soldiers
    Returns:
        bool: True if the array contains a bad group, otherwise False
    """
    g = arr[0]
    for x in arr[1:]:
        g = gcd(g, x)
    return g == 1

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    n = int(data[0])
    arr = list(map(int, data[1:n+1]))

    result = find_bad(arr)
    print("true" if result else "false")

if __name__ == "__main__":
    main()