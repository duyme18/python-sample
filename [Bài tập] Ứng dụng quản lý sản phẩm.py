list_item = {1: {'name': 'John'},
             2: {'name': 'Marie'}}


def get_item(items, item_id):
    if item_id in items:
        print(items[item_id])
    else:
        print(item_id, ' not exists')


def update_item(items, item_id, new_name):
    for k in items:
        if item_id == k:
            items[item_id] = new_name
    else:
        items[item_id] = {}
        items[item_id]['name'] = new_name
        print(items)


def delete_item(items, item_id):
    for k in items:
        if item_id == k:
            del items[item_id]
            print('delete success')
            print(items)
    else:
        print(item_id, ' not exists')


while True:
    print("Option:\n"
          "1. Get Item\n"
          "2. Update Item\n"
          "3. Delete Item\n"
          "0. Exit")
    option = int(input('Option: '))
    if option == 1:
        input_id = int(input('Enter id: '))
        get_item(list_item, input_id)
    elif option == 2:
        input_id = int(input('Enter id: '))
        input_name = input('Enter name: ')
        update_item(list_item, input_id, input_name)
    elif option == 3:
        input_id = int(input('Enter id: '))
        delete_item(list_item, input_id)
    elif option == 4:
        break
    else:
        print('invalid input')
