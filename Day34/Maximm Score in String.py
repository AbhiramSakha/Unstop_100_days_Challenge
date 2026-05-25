def calculate_max_score(n, s):
    MOD = 10**9 + 7
    
    # Convert chars to values and sort ascending
    vals = sorted(ord(c) - 96 for c in s)
    
    power = 1
    ans = 0
    
    for v in vals:
        ans = (ans + v * power) % MOD
        power = (power * 26) % MOD
    
    return ans

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])
    s = data[1]
    
    result = calculate_max_score(n, s)
    print(result)

if __name__ == "__main__":
    main()
                      