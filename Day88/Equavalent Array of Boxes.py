def user_logic(arr1, arr2):
    return ''.join(arr1) == ''.join(arr2)

if __name__ == '__main__':
    import sys

    n = int(raw_input())
    arr1 = raw_input().strip().split()

    m = int(raw_input())
    arr2 = raw_input().strip().split()

    print('true' if ''.join(arr1) == ''.join(arr2) else 'false')