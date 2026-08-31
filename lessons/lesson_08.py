from collections import Counter

def simple_list():
    products = ["Laptop", "Phone", "Tablet", "Monitor"]

    print(products)
    print(products[0])
    print(products[-1])
    print(len(products))
    products.append("Keyboard")
    print(products)

def nested_list():
    products_by_category = [
    ["Laptop", "MacBook"],
    ["Phone", "iPhone", "Samsung"],
    ["Monitor", "Dell", "LG"]
    ]

    print(products_by_category)
    print(products_by_category[0][0])
    print(products_by_category[1][1])
    print(products_by_category[2][2])
    
def transform_nexted_list_to_list():
    products_by_category = [
    ["Laptop", "MacBook"],
    ["Phone", "iPhone", "Samsung"],
    ["Monitor", "Dell", "LG"]
    ]
    products =[]
    for category in products_by_category:
        for product in category:
            products.append(product)
    print(products)

from collections import Counter


def compare_lists():
    expected = ["Laptop", "Phone", "Phone", "Monitor"]
    actual = ["Laptop", "Phone", "Keyboard", "Monitor"]

    counter_expected = Counter(expected)
    counter_actual = Counter(actual)

    missing = counter_expected - counter_actual
    unexpected = counter_actual - counter_expected

    print("---------------- Compare_list_test ----------------")
    print("Missing:", missing)
    print("Unexpected:", unexpected)

    print("---------------- Compare_list_of_elements ----------------")
    print("Missing elements:", list(missing.elements()))
    print("Unexpected elements:", list(unexpected.elements()))

def list_of_dicts():
    products = [
        {"id": 1, "name": "Laptop", "price": 1000},
        {"id": 2, "name": "Phone", "price": 500},
        # {"id": 3, "name": "Monitor", "price": 300},
    ]
    actual_names = []

    for product in products:
        actual_names.append(product["name"])

    expected_names = ["Laptop", "Phone", "Monitor"]

    if actual_names == expected_names:
        print("PASS")
    else:
        missing_names = Counter(expected_names)-Counter(actual_names)
        missing_list_names = list(missing_names.elements())
        print(missing_list_names)
        unexpected_names = Counter(actual_names)-Counter(expected_names)
        unexpected_list_names = list(unexpected_names.elements())
        print(unexpected_list_names)

def compare_nexted_list():
    expected_list =  [
            ["Laptop"],
            ["Phone"],
    ]
    actual_list = [
        ["Laptop"],
        ["Phone"],
        ["Keyboard"]
    ]
    result = []

    if len(expected_list) != len(actual_list):
        result = {
            "status": "FAIL",
            "error": "Different number of categories",
            "expected_count": len(expected_list),
            "actual_count": len(actual_list)
        }

    for index, (actual_names, expected_names) in enumerate(
        zip(actual_list, expected_list)
    ):

        missing_names = Counter(expected_names) - Counter(actual_names)
        unexpected_names = Counter(actual_names) - Counter(expected_names)

        if not missing_names and not unexpected_names:
            status = {
                "category": index + 1,
                "status": "PASS"
            }

        else:
            status = {
                "category": index + 1,
                "status": "FAIL",
                "missing": list(missing_names.elements()),
                "unexpected": list(unexpected_names.elements())
            }

        result.append(status)
    print(result)

    return result
    
    

        
# simple_list()
# nested_list()
# transform_nexted_list_to_list()
# compare_lists()
# list_of_dicts()
compare_nexted_list()