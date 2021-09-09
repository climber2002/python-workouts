def ubbi_dubbi(word):
    res = ''
    for c in word:
        if c in 'aeiou':
            res += 'ub'
        res += c
    return res

print(ubbi_dubbi('program'))