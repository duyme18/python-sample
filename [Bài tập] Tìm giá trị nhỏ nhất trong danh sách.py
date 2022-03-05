
def find_min(list_number):
    result = list_number[0]
    for num in list_number:
        if result > num:
            result = num
    return result

list_num = [0, 2, 6, 3, 2, 6, 8, 34, 32, 21, 43, 2, 123]


min_number = find_min(list_num)
print("Min number: ", min_number)
