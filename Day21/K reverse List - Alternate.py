class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapPairs(head):
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    while prev.next and prev.next.next:
        first = prev.next
        second = prev.next.next

        # Swap nodes
        prev.next = second
        first.next = second.next
        second.next = first

        # Move prev two nodes ahead
        prev = first

    return dummy.next


def stringToListNode(input):
    input = input[1:-1].strip()
    if not input:
        return None
    # Handle both comma-separated and space-separated input
    node_values = [int(x.strip()) for x in input.replace(',', ' ').split() if x.strip()]
    dummy_root = ListNode(0)
    ptr = dummy_root
    for val in node_values:
        ptr.next = ListNode(val)
        ptr = ptr.next
    return dummy_root.next


def listNodeToString(node):
    if not node:
        return '[]'
    result = '[' + ', '.join(map(str, iter_list(node))) + ']'
    return result


def iter_list(node):
    while node:
        yield node.val
        node = node.next


if __name__ == '__main__':
    import sys
    input = sys.stdin.read().strip()
    head = stringToListNode(input)
    swapped_head = swapPairs(head)
    print(listNodeToString(swapped_head))