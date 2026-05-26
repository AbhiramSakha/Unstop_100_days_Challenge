def is_prime_digit(d):
    return d in {'2', '3', '5', '7'}

def alphanumeric_transform(n, s):
    digits = [int(ch) for ch in s if ch.isdigit()]
    primes = [d for d in digits if is_prime_digit(str(d))]

    result = []
    
    if primes:
        unique_number = sum(primes) // len(primes)
    else:
        unique_number = None  # We’ll handle this case separately

    for ch in s:
        if ch.isdigit():
            digit = int(ch)
            if unique_number is not None:
                idx = digit % unique_number
            else:
                idx = digit
            result.append(chr(ord('a') + idx))
        else:
            result.append(ch)

    return ''.join(result)

# Input
n = int(input())
s = input().strip()

# Output
print(alphanumeric_transform(n, s))
                            