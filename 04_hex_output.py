def hex_output(hex_str):
    n = 0
    for c in hex_str:
        n = n * 16 + int(c, 16)
    return n

print(hex_output('50'))
print(hex_output('ABC'))