def calculate_valid_pins(n):
    MOD = 10**9 + 7

    even_positions = (n + 1) // 2   # indices 0,2,4,...
    odd_positions = n // 2          # indices 1,3,5,...

    return (pow(5, even_positions, MOD) * pow(4, odd_positions, MOD)) % MOD

if __name__ == "__main__":
    n = int(input().strip())
    result = calculate_valid_pins(n)
    print(result)