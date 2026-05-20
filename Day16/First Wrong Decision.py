def FirstWrongDecision(s):
    # Find the index of the first 'W'
    index = s.find('W')
    return index  # Returns -1 if 'W' is not found automatically

if __name__ == '__main__':
    str = input()
    print(FirstWrongDecision(str))