# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def generate_pascals_row(n):
    row = []
    for k in range(n + 1):
        value = math.comb(n, k)  # Efficient binomial coefficient
        row.append(value)
    return row

def main():
    n = int(input().strip())
    result = generate_pascals_row(n)
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()