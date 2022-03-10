products = {
    'smart-phone': 50,
    'iphone': 100,
    'samsung': 200,
    'nokia': 300
}

def display_product(product_db, price):
    for item in product_db:
        if product_db[item] <= price:
            print(item, ' : ', product_db[item])

input_price = int(input('enter price: '))

display_product(products, input_price)