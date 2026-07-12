class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def countPairs(head, V):
    freq = {}
    count = 0
    curr = head

    while curr:
        complement = V - curr.data
        if complement in freq:
            count += freq[complement]
        freq[curr.data] = freq.get(curr.data, 0) + 1
        curr = curr.next

    return count


def buildLinkedList(arr):
    if not arr:
        return None
    head = Node(arr[0])
    curr = head
    for x in arr[1:]:
        curr.next = Node(x)
        curr = curr.next
    return head


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    V = int(input())

    head = buildLinkedList(arr)
    print(countPairs(head, V))


if __name__ == "__main__":
    main()