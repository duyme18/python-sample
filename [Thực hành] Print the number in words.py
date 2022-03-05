numbers = input('nhap so bat ky: ')
text = ('không', 'một', 'hai', 'ba', 'bốn', 'năm', 'sáu', 'bảy', 'tám', 'chín')
for num in numbers:
    print(text[int(num)], end=' ')
