import pytest
from pydantic import BaseModel

from api.product_api import ProductApi
from models.products_response import ProductsResponse
from helpers.response_validator import ResponseValidator
from helpers.product_payload_generator import ProductPayloadGenerator


def test_create_product(product_api):

   
    payload = ProductPayloadGenerator.collect_products_data(product_api)
    print("\n\nPayload: ", payload)

    new_product_response = product_api.create_product(payload)

    assert new_product_response.price == payload["price"], \
        f"price mismatch: response={new_product_response.price}, payload={payload['price']}"

    assert new_product_response.brand.id == payload["brand_id"], \
    f"brand_id mismatch: response={new_product_response.brand.id}, payload={payload['brand_id']}"

    assert new_product_response.category.id == payload["category_id"], \
        f"category_id mismatch: response={new_product_response.category.id}, payload={payload['category_id']}"

    assert new_product_response.co2_rating == payload["co2_rating"], \
        f"co2_rating mismatch: response={new_product_response.co2_rating}, payload={payload['co2_rating']}"

    assert new_product_response.is_location_offer == payload["is_location_offer"], \
        f"is_location_offer mismatch: response={new_product_response.is_location_offer}, payload={payload['is_location_offer']}"

    assert new_product_response.is_rental == payload["is_rental"], \
        f"is_rental mismatch: response={new_product_response.is_rental}, payload={payload['is_rental']}"

    assert new_product_response.name == payload["name"], \
        f"name mismatch: response={new_product_response.name}, payload={payload['name']}"

    assert new_product_response.product_image.id == payload["product_image_id"], \
        f"product_image_id mismatch: response={new_product_response.product_image.id}, payload={payload['product_image_id']}"

    assert new_product_response.in_stock == payload["stock"], \
        f"stock mismatch: response={new_product_response.in_stock}, payload={payload['stock']}"

    assert new_product_response.is_eco_friendly == payload["is_eco_friendly"], \
        f"is_eco_friendly mismatch: response={new_product_response.is_eco_friendly}, payload={payload['is_eco_friendly']}"

  

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
   