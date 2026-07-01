class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

def segregate_list(head, x):
    if head is None:
        return head

    div_dummy = Node(0)
    non_dummy = Node(0)

    div_tail = div_dummy
    non_tail = non_dummy

    curr = head

    while curr:
        nxt = curr.next
        curr.next = None

        if curr.data % x == 0:
            div_tail.next = curr
            div_tail = curr
        else:
            non_tail.next = curr
            non_tail = curr

        curr = nxt

    div_tail.next = non_dummy.next

    if div_dummy.next:
        return div_dummy.next
    return non_dummy.next

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])
    elements = list(map(int, data[1:n+1]))
    x = int(data[n+1])
    
    ll = LinkedList()
    for element in elements:
        ll.push(element)
    
    ll.head = segregate_list(ll.head, x)
    ll.print_list()

if __name__ == "__main__":
    main()