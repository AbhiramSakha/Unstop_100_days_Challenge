# Python 3
class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

def minChanges(head, n):
    """
    Write your logic here.
    Parameters:
        head (Node): Head of the linked list
        n (int): Size of the linked list
    Returns:
        int: Minimum number of changes to make the linked list in non-decreasing order
    """
    pass

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # First input is the integer N
    values = list(map(int, data[1:]))  # Remaining input is the heights of the students
    
    # Create the linked list
    head = Node(values[0])
    temp = head
    for val in values[1:]:
        temp.next = Node(val)
        temp = temp.next
    
    # Call user logic function and print the output
    result = minChanges(head, n)
    print(result)

if __name__ == "__main__":
    main()