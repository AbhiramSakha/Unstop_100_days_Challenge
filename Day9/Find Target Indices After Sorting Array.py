# Enter your code here. Read input from STDIN. Print output to STDOUT
def find_target_indices():
    N = int(input())
    A = list(map(int, input().split()))
    K = int(input())

    A.sort()

    indices = [i for i, val in enumerate(A) if val == K]

    print(len(indices))
    print(*indices)

# Run the function
find_target_indices()
                       