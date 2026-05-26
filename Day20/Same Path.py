class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


def check(l1, l2):
    """
    Parameters:
        l1 (Node): Head of the first linked list
        l2 (Node): Head of the second linked list
    Returns:
        int: 1 if the linked lists merge, otherwise 0
    """
    visited = set()

    # Store nodes of first linked list
    current = l1
    while current:
        visited.add(current)
        current = current.next

    # Check nodes of second linked list
    current = l2
    while current:
        if current in visited:
            return 1
        current = current.next

    return 0


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])
    m = int(data[1])
    
    map = {}
    
    # Create first linked list
    l1 = Node(0)
    temp = l1
    index = 2
    for _ in range(n):
        t = int(data[index])
        index += 1
        if t in map:
            curr = map[t]
        else:
            curr = Node(t)
            map[t] = curr
        temp.next = curr
        temp = temp.next
    l1 = l1.next
    
    # Create second linked list
    l2 = Node(0)
    temp = l2
    for _ in range(m):
        t = int(data[index])
        index += 1
        if t in map:
            curr = map[t]
        else:
            curr = Node(t)
            map[t] = curr
        temp.next = curr
        temp = temp.next
    l2 = l2.next
    
    result = check(l1, l2)
    print(result)


if __name__ == "__main__":
    main()