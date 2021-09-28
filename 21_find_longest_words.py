import os

def find_longest_word(filename):
    longest_length = 0
    longest_word = ''
    for line in open(filename):
        words = line.split(' ')
        for word in words:
            if len(word) > longest_length:
                longest_length = len(word)
                longest_word = word
    return longest_word

def find_all_longest_words(dirname):
    return {
        filename: find_longest_word(os.path.join(dirname, filename))
            for filename in os.listdir(dirname) if os.path.isfile(os.path.join(dirname, filename))
    }

print(find_all_longest_words('.'))