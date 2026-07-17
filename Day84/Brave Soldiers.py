def count_brave_soldiers(n):
    """
    Write your logic here.
    Parameters:
        n (int): The number of soldiers in the army
    Returns:
        int: The count of brave soldiers
    """
    if n < 2:
        return 0

    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    i = 2
    while i * i <= n:
        if is_prime[i]:
            j = i * i
            while j <= n:
                is_prime[j] = False
                j += i
        i += 1

    return sum(is_prime)


import sys
input = sys.stdin.read
n = int(input().strip())

# Call the user logic function and print the output
result = count_brave_soldiers(n)
print(result)