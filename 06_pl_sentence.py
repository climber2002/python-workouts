def pig_latin(word):
    if word[0] in 'aeiou':
        return f'{word}way'

    return f'{word[1:]}{word[0]}ay'

def pl_sentence(sentence):
    return ' '.join([pig_latin(word) for word in sentence.split()])

print(pl_sentence('this is a test translation'))