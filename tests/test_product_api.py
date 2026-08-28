import pytest
from pydantic import BaseModel

from api.product_api import ProductApi
from models.products_response import ProductsResponse
from helpers.response_validator import ResponseValidator

def test_products(product_api):

    products = product_api.products()

    for product in products.data:
        assert isinstance(product.id, str)
        assert product.id

        assert product.name
        assert product.description

        assert product.price >= 0

        assert isinstance(product.in_stock, bool)

        assert product.category.id
        assert product.category.name
        assert product.category.slug

        assert product.brand.id
        assert product.brand.name


def test_products_filter_by_brand(product_api):
    list_of_brands = {}

    for page in range(product_api.products().last_page):
        products = product_api.products(page=page)

        for product_data in products.data:
            list_of_brands[product_data.brand.id] = product_data.brand.name

    for brand_id, brand_name in list_of_brands.items():
        products = product_api.products(brand=brand_id)

        assert products.data

        for product in products.data:
            assert product.brand.id == brand_id
            assert product.brand.name == brand_name


def test_products_have_valid_data(product_api):

    products = product_api.products()

    for product in products.data:
        assert isinstance(product.id, str)
        assert product.id

        assert product.name
        assert product.description
        assert product.price >= 0
        assert isinstance(product.in_stock, bool)


def test_products_pagination(product_api):

    products_page_1 = product_api.products(page=1)
    products_page_2 = product_api.products(page=2)

    assert products_page_1.current_page == 1
    assert products_page_2.current_page == 2

    assert products_page_1.total > 0
    assert products_page_2.total > 0

    assert len(products_page_1.data) <= products_page_1.per_page
    assert len(products_page_2.data) <= products_page_2.per_page

    assert products_page_1.data != products_page_2.data


def test_products_with_auth_token(product_api, auth_token):

    product_api.client.set_token(auth_token)

    products = product_api.products()

    for product in products.data:
        assert isinstance(product.id, str)
        assert product.id

        assert product.name
        assert product.description
        assert product.price >= 0

def test_comparing_products_and_product_api_by_id(product_api):

    for page in range(product_api.products().last_page):
        products = product_api.products(page=page)

        for product_data in products.data:
            product_id = product_data.id
            product_by_id = product_api.product_by_id(product_id)

            ResponseValidator.assert_models_equal(
                product_data,
                product_by_id
            )
   