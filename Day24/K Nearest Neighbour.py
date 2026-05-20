def find_k_nearest_points(points, k):
    """
    Write your logic here.
    Parameters:
        points (list of lists): List of [x, y] coordinates of points
        k (int): Number of nearest points to find
    Returns:
        list of lists: K nearest points to the origin
    """
    pass

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # Number of points
    k = int(data[1])  # Number of nearest points to find
    
    points = []
    index = 2
    for _ in range(n):
        x = int(data[index])
        y = int(data[index + 1])
        points.append([x, y])
        index += 2
    
    # Call user logic function and get the result
    result = find_k_nearest_points(points, k)
    
    # Print the result
    for point in result:
        print(point[0], point[1])

if __name__ == "__main__":
    main()