def user_logic(n):
    return n ^ 0xFFFFFFFF

if __name__ == '__main__':
    n = int(input())
    print(user_logic(n))