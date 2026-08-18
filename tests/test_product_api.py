import pytest

from api.product_api import ProductApi
from models.products_response import ProductsResponse

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

@pytest.mark.parametrize(
    "brand",
    [
        "01M0B3XVZF97SFESM28ZBBXKEA",
        "01M0B3XVZF97SFESM28ZBBXKEB",
    ]
)
def test_products_filter(product_api, brand):

    products = product_api.products(brand=brand)

    assert products.data

    for product in products.data:
        assert product.brand.id == brand


@pytest.mark.parametrize(
    "brand, name",
    [
        (
            "01M0B3XVZF97SFESM28ZBBXKEA",
            "ForgeFlex Tools"
        ),
        (
            "01M0B3XVZF97SFESM28ZBBXKEB",
            "MightyCraft Hardware"
        ),
    ]
)
def test_products_filter_by_brand(product_api, brand, name):

    products = product_api.products(brand=brand)

    assert products.data

    for product in products.data:
        assert product.brand.id == brand
        assert product.brand.name == name


@pytest.mark.parametrize(
    "category_id, category_name",
    [
        (
            "01M0B3XW9GD6DB48DMMH5CZP2H",
            "Hammer"
        ),
    ]
)
def test_products_filter_by_category(
    product_api,
    category_id,
    category_name
):

    products = product_api.products(category=category_id)

    assert products.data

    for product in products.data:
        assert product.category.id == category_id
        assert product.category.name == category_name


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