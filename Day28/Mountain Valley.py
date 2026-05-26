class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def countNodes(head):
    if not head or not head.next or not head.next.next:
        return 0

    count = 0
    prev = head
    curr = head.next

    while curr.next:
        if curr.data > prev.data and curr.data > curr.next.data:
            count += 1

        prev = curr
        curr = curr.next

    return count

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])
    elements = list(map(int, data[1:]))
    
    head = None
    tail = None
    
    for elem in elements:
        new_node = Node(elem)
        if head is None:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node
    
    result = countNodes(head)
    print(result)

if __name__ == "__main__":
    main()