def count_ones_in_binary(n):
    count = 0
    for i in range(1, n + 1):
        count += bin(i).count('1')
    return count

if __name__ == "__main__":
    n = int(input())  # Read the integer N
    result = count_ones_in_binary(n)  # Call the function
    print(result)  # Output the result
                            