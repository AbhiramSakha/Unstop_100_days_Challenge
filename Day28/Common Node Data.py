# Enter your code here. Read input from STDIN. Print output to STDOUT
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def firstCommonNode(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)

    i = n1 - 1
    j = n2 - 1

    ans = -1

    while i >= 0 and j >= 0 and arr1[i] == arr2[j]:
        ans = arr1[i]
        i -= 1
        j -= 1

    return ans


def main():
    import sys
    input = sys.stdin.read

    data = input().strip().split()

    n1 = int(data[0])
    n2 = int(data[1])

    arr1 = list(map(int, data[2:2 + n1]))
    arr2 = list(map(int, data[2 + n1:2 + n1 + n2]))

    print(firstCommonNode(arr1, arr2))


if __name__ == "__main__":
    main()
                            