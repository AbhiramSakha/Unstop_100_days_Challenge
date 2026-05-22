def sum_of_depths(n, edges):
    """
    Write your logic here.
    Parameters:
        n (int): Number of nodes in the tree
        edges (list of tuple): List of edges where each edge is represented as a tuple (A, B)
    Returns:
        int: The sum of the depths of all nodes in the tree
    """
    pass

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # First input is the number of nodes
    edges = []
    index = 1
    for _ in range(n - 1):
        a = int(data[index])
        b = int(data[index + 1])
        edges.append((a, b))
        index += 2
    
    # Call user logic function and print the output
    result = sum_of_depths(n, edges)
    print(result)

if __name__ == "__main__":
    main()