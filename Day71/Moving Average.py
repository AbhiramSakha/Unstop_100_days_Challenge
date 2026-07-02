# Python 3
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

def user_logic(linked_list, window_size):
    arr = []
    curr = linked_list.head
    while curr:
        arr.append(curr.data)
        curr = curr.next

    n = len(arr)

    if window_size > n or window_size <= 0:
        return ""

    window_sum = sum(arr[:window_size])
    ans = []

    for i in range(window_size, n + 1):
        avg = window_sum / window_size
        s = "{:.2f}".format(avg).rstrip("0").rstrip(".")
        ans.append(s)

        if i < n:
            window_sum += arr[i] - arr[i - window_size]

    return " ".join(ans)

def main():
    import sys
    input = sys.stdin.read

    data = input().strip().split()

    n = int(data[0])
    elements = list(map(int, data[1:n + 1]))
    window_size = int(data[n + 1])

    linked_list = LinkedList()
    for x in elements:
        linked_list.push(x)

    result = user_logic(linked_list, window_size)
    print(result)

if __name__ == "__main__":
    main()