def min_operations_to_bst(arr):
    n = len(arr)
    inorder = []

    def dfs(i):
        if i >= n:
            return
        dfs(2 * i + 1)
        inorder.append(arr[i])
        dfs(2 * i + 2)

    dfs(0)

    operations = 0
    prev = -1

    for i in range(len(inorder)):
        if inorder[i] <= prev:
            operations += (prev + 1 - inorder[i])
            prev += 1
        else:
            prev = inorder[i]

    return operations


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(min_operations_to_bst(arr))


if __name__ == "__main__":
    main()