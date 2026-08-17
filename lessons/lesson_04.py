products = []


def create_product(name, price, available):
    product = {
        "name": name,
        "price": price,
        "available": available
    }
    return product


def is_product_available(product):
    if product["available"]:
        print(f"{product['name']} is available")
    else:
        print(f"{product['name']} is not available")


products.append(create_product("laptop", 1500, True))
products.append(create_product("tablet", 1000, False))

print(products)

is_product_available(products[0])
is_product_available(products[1])