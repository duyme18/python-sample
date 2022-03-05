gadgets = ['Mobile', 'Laptop', 100, 'Camera', 310.28, 'Speakers', 27.00, 'Television', 1000, 'Laptop Case', 'Camera Lens']

list_num = []
list_str = []

for i in gadgets:
    if isinstance(i, str):
        list_str.append(i)
    else:
        list_num.append(i)

print(list_str)
print(list_num)
print('sort string tang dan ', list_str.sort())
print('sort string giam dan ', list_str.sort(reverse=False))
# Sắp xếp list chứa số
list_num.sort()
print("List chứa số theo thứ tự tăng dần= ", list_num)
list_num.sort(reverse=True)
print("List chứa số theo thứ tự giảm dần= ", list_num)