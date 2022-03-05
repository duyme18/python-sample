def count_chars(txt):
    result = 0
    for char in txt:
        result += 1
    return result


txt = input('nhap chuoi bat ky: ')
print(count_chars(txt))
