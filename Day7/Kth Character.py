# Enter your code here. Read input from STDIN. Print output to STDOUT
def kth_char_after_reverse(n, k, s):
    # Directly access the (n - k)th character of original string
    return s[n - k]

# Input reading
n, k = map(int, input().split())
s = input().strip()

print(kth_char_after_reverse(n, k, s))
                            