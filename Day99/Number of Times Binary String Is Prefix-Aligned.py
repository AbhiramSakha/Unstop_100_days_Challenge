def numTimesAllBlue(flips):
    """
    Write your logic here.
    Parameters:
        flips (list): List of integers representing the binary string flips
    Returns:
        int: Number of times the binary string is prefix-aligned
    """
    ans = 0
    mx = 0

    for i, x in enumerate(flips, 1):
        mx = max(mx, x)
        if mx == i:
            ans += 1

    return ans


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])
    flips = list(map(int, data[1:]))

    result = numTimesAllBlue(flips)
    print(result)

if __name__ == "__main__":
    main()