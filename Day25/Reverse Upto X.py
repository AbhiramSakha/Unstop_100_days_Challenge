#!/bin/python3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def print(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next

    def push(self, data):
        if self.head is None:
            temp = Node(data)
            self.head = temp
            self.tail = temp
        else:
            temp = Node(data)
            self.tail.next = temp
            self.tail = temp

def reverseLinkedListUpToX(ll, x):
    # User needs to implement the logic here
    pass

if __name__ == '__main__':
    ll = LinkedList()
    n = int(input())
    for _ in range(n):
        t = int(input())
        ll.push(t)
    x = int(input())
    reverseLinkedListUpToX(ll, x)
    ll.print()