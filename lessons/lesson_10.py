from lessons.lesson_11 import ApiError

def divide_numbers(a,b):
    result = 0
    try:
        return a/b 
    except ZeroDivisionError:
        return "Can not divide by zero"
    

def divide_numbers_2(a, b):
    print("Test Started")

    try:
        print("Test is running")
        result = a / b

    except ZeroDivisionError:
        print("Test failed")
        result = "Cannot divide by zero"

    finally:
        print("Cleanup")
    return result

def get_number(value):
    n = None
    try:
        n = int(value)
    except ValueError as e:
        print("Conversion failed")
        print ("Error: ", e)
        return n 
    else:
        print("Conversion successful")
        return n  
    finally:
        print("cleanup")

def check_age(age):
    if age >= 18:
        print("Access granted")
    else:
        raise ValueError("Age must be 18 or older")


def get_product(prod_id):
    
    if prod_id <= 0:
            raise ApiError("Product ID must be greater than 0") 
    return f"Product {prod_id}"

try:
    result = get_product(0)
    print(result)

except ApiError as e:
    print("LOG:", e)
    print(e.msg)