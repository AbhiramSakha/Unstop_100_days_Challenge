from collections import Counter

def sum_of_good_words(n, words, chars):
    char_count = Counter(chars)
    total_length = 0

    for word in words:
        word_count = Counter(word)
        if all(word_count[c] <= char_count.get(c, 0) for c in word_count):
            total_length += len(word)
    
    return total_length

n = int(input().strip())
words = [input().strip() for _ in range(n)]
chars = input().strip()

print(sum_of_good_words(n, words, chars))