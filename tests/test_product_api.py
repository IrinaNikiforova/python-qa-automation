import pytest

from api.product_api import ProductApi
from models.products_response import ProductsResponse

def test_products(product_api):

    products = product_api.products()

    for product in products.data:
        assert product.id > 0
        assert product.name
        assert product.price >= 0
        assert product.stock >= 0
        assert product.category.id == product.category_id
        assert product.brand.id == product.brand_id

@pytest.mark.parametrize("brand", [ 1, 2 ])
def test_products_filter(product_api, brand):
    
    products = product_api.products(brand=brand)

    for product in products.data:
        assert product.brand.id == brand

@pytest.mark.parametrize(
    "brand, name",
    [
        ("1", "Brand name 1"),
        ("2", "Brand name 2"),
    ]
)
def test_products_filter_by_brand(product_api, brand, name):
    
    products = product_api.products(brand=brand)

    for product in products.data:
        assert product.brand.name == name

@pytest.mark.parametrize(
    "id , name",
    [
        (3, "Hammer"),
        (4, "Hand Saw"),
    ]
)
def test_products_filter_by_category(product_api, id, name):

    products = product_api.products(category=id)

    assert products.data

    for product in products.data:
        assert product.category.id == id
        assert product.category.name == name

def test_products_have_valid_data(product_api):
    products = product_api.products()

    for product in products.data:
        assert product.id > 0
        assert product.name
        assert product.description
        assert product.price >= 0

def test_products_pagination(product_api):

    products_page_1 = product_api.products(page=1)

    products_page_2 = product_api.products(page=2)

    assert products_page_1.current_page == 1
    assert products_page_2.current_page == 2

    assert len(products_page_1.data) <= products_page_1.per_page
    assert len(products_page_2.data) <= products_page_2.per_page

    assert products_page_1.data != products_page_2.data

def test_products_with_auth_token(product_api, auth_token):
    product_api.client.set_token(auth_token)
    products = product_api.products()

    for product in products.data:
        assert product.id > 0
        assert product.name
        assert product.description
        assert product.price >= 0

