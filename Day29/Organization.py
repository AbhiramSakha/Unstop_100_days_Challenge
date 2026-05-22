def calculate_subordinates(V, hierarchy):
    """
    Write your logic here.
    Parameters:
        V (int): Number of employees
        hierarchy (list): List of integers where the i-th integer represents the boss of the (i+1)th employee
    Returns:
        list: List of integers where the ith integer represents the number of employees working under the ith employee
    """
    pass

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    V = int(data[0])  # Number of employees
    hierarchy = list(map(int, data[1:]))  # Boss of each employee
    
    # Call user logic function and get the result
    result = calculate_subordinates(V, hierarchy)
    
    # Print the result as space-separated integers
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()