from bisect import bisect_right

def user_logic(n, arr, b):
    """
    Write your logic here.
    Parameters:
        n (int): Number of chapters in both syllabuses
        arr (list): List of intrinsic values for syllabus 1
        b (list): List of intrinsic values for syllabus 2
    Returns:
        int: Highest interest value among both available syllabuses
    """
    
    arr_sorted = sorted(arr)
    b_sorted = sorted(b)
    
    interest1 = 0
    for x in arr:
        interest1 += bisect_right(b_sorted, x)
    
    interest2 = 0
    for x in b:
        interest2 += bisect_right(arr_sorted, x)
    
    return max(interest1, interest2)


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])
    arr = list(map(int, data[1:n+1]))
    b = list(map(int, data[n+1:2*n+1]))
    
    result = user_logic(n, arr, b)
    print(result)

if __name__ == "__main__":
    main()
                           