list_num = [2, 5, 7, 34, 7, 4, 2, 76, 879, 3, 24, 55, 6456, 345, 2345, 2345, 46, 456, 756, 765, 856, 8]

print('Danh sách hiện tại:', list_num)


def sort(numbers):
    length = len(numbers)

    for i in range(0, length - 1):
        for j in range(i + 1, length):
            if numbers[i] > numbers[j]:
                temp = numbers[i]
                numbers[i] = numbers[j]
                numbers[j] = temp
    return numbers


sort(list_num)
print('Danh sách sắp xếp theo thứ tự tăng dần: ', sort(list_num))
print(list_num[-4])
print('2 số lớn nhất trong mảng là {} và {}.'.format(list_num[-2], list_num[-1]))
