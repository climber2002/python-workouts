def mysum(*numbers):
    sum = 0
    for n in numbers:
        sum += n
    return sum

print(mysum(10, 20, 30, 40))