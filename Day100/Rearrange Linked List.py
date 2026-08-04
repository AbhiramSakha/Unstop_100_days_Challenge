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
        temp = self.head
        result = []

        while temp:
            result.append(temp.data)
            temp = temp.next

        print(" ".join(map(str, result)))

def user_logic(linked_list):
    """
    Rearrange nodes as:
    positions 1,4,7...
    then 2,5,8...
    then 3,6,9...
    """

    groups = [[], [], []]

    temp = linked_list.head
    idx = 0

    while temp:
        groups[idx % 3].append(temp.data)
        temp = temp.next
        idx += 1

    new_ll = LinkedList()

    for group in groups:
        for val in group:
            new_ll.push(val)

    return new_ll

def main():
    import sys

    input = sys.stdin.read
    data = input().strip().split()

    n = int(data[0])

    elements = list(map(int, data[1:]))

    ll = LinkedList()

    for element in elements:
        ll.push(element)

    modified_ll = user_logic(ll)

    modified_ll.print_list()

if __name__ == "__main__":
    main()