class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def user_logic(head):
    if head is None:
        return None

    curr = head
    while curr is not None and curr.next is not None:
        if curr.val == curr.next.val:
            curr.next = curr.next.next
        else:
            curr = curr.next

    return head


def main():
    import sys

    data = sys.stdin.read().strip().split()

    if not data:
        return

    n = int(data[0])

    if n == 0:
        print 0
        return

    arr = map(int, data[1:1 + n])

    head = Node(arr[0])
    curr = head
    for x in arr[1:]:
        curr.next = Node(x)
        curr = curr.next

    head = user_logic(head)

    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next

    print len(result)
    if result:
        print " ".join(map(str, result))


if __name__ == "__main__":
    main()