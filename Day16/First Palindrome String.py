def first_palindromic_string(arr):
    for word in arr:
        if word == word[::-1]:
            return word
    return ""

if __name__ == '__main__':
    N = int(input())
    A = input().split()
    print(first_palindromic_string(A))