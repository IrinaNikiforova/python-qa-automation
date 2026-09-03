import pytest
import time

from helpers.response_validator import ResponseValidator


def test_create_product(created_product):

    payload, response = created_product

    assert response.price == payload["price"], \
        f"price mismatch: response={response.price}, payload={payload['price']}"

    assert response.brand.id == payload["brand_id"], \
        f"brand_id mismatch: response={response.brand.id}, payload={payload['brand_id']}"

    assert response.category.id == payload["category_id"], \
        f"category_id mismatch: response={response.category.id}, payload={payload['category_id']}"

    assert response.co2_rating == payload["co2_rating"], \
        f"co2_rating mismatch: response={response.co2_rating}, payload={payload['co2_rating']}"

    assert response.is_location_offer == payload["is_location_offer"], \
        f"is_location_offer mismatch: response={response.is_location_offer}, payload={payload['is_location_offer']}"

    assert response.is_rental == payload["is_rental"], \
        f"is_rental mismatch: response={response.is_rental}, payload={payload['is_rental']}"

    assert response.name == payload["name"], \
        f"name mismatch: response={response.name}, payload={payload['name']}"

    assert response.product_image.id == payload["product_image_id"], \
        f"product_image_id mismatch: response={response.product_image.id}, payload={payload['product_image_id']}"

    assert response.in_stock == payload["stock"], \
        f"stock mismatch: response={response.in_stock}, payload={payload['stock']}"

    assert response.is_eco_friendly == payload["is_eco_friendly"], \
        (
            f"is_eco_friendly mismatch: "
            f"response={response.is_eco_friendly}, "
            f"payload={payload['is_eco_friendly']}"
        )


def test_created_product_is_available_by_id(
    product_api,
    created_product
):

    payload, response = created_product

    product_id = response.id

    product_by_id = product_api.product_by_id(product_id)

    assert product_by_id.id == product_id, \
        (
            f"Product ID mismatch: "
            f"expected={product_id}, "
            f"actual={product_by_id.id}"
        )

    ResponseValidator.assert_models_equal(
        response,
        product_by_id
    )


@pytest.mark.xfail(
    reason=(
        "BUG: Product created through POST /products is available "
        "through GET /products/{id}, but does not reliably appear "
        "in the paginated GET /products response."
    ),
    strict=False
)
def test_created_product_is_available_in_products(
    product_api,
    created_product
):

    payload, response = created_product

    product_id = response.id
    found_product = None
    existing_product = None

    for attempt in range(2):

        print(f"\n===== ATTEMPT {attempt + 1} =====")

        first_page = product_api.products()

        print(f"Total products: {first_page.total}")
        print(f"Total pages: {first_page.last_page}")

        for page in range(1, first_page.last_page + 1):

            products_response = product_api.products(page=page)

            print(
                f"Checking page {page}: "
                f"{len(products_response.data)} products"
            )

            if existing_product is None and products_response.data:
                existing_product = products_response.data[0]

            for product in products_response.data:

                if product.id == product_id:
                    found_product = product
                    break

            if found_product is not None:
                break

        if found_product is not None:
            break

        print("Created product was not found. Waiting 1 second...")
        time.sleep(1)

    print("\n===== CREATED PRODUCT =====")
    print(response.model_dump_json(indent=2))

    if found_product is not None:

        print("\n===== PRODUCT FOUND IN GET /products =====")
        print(found_product.model_dump_json(indent=2))

        ResponseValidator.assert_models_equal(
            response,
            found_product
        )

    else:

        print("\n===== PRODUCT FOUND IN GET /products =====")

        if existing_product is not None:
            print(existing_product.model_dump_json(indent=2))
        else:
            print("No products were returned")

        pytest.fail(
            f"BUG: Created product with id={product_id} "
            f"was not found in GET /products after 10 attempts."
        )


def test_products(product_api):

    products = product_api.products()

    for product in products.data:

        assert isinstance(product.id, str)
        assert product.id

        assert product.name

        if product.description is not None:
            assert product.description

        assert product.price >= 0

        if product.in_stock is not None:
            assert isinstance(product.in_stock, bool)

        assert product.category.id
        assert product.category.name
        assert product.category.slug

        assert product.brand.id
        assert product.brand.name


def test_products_filter_by_brand(product_api):

    list_of_brands = {}

    first_page = product_api.products()

    for page in range(1, first_page.last_page + 1):

        products = product_api.products(page=page)

        for product in products.data:

            list_of_brands[product.brand.id] = product.brand.name

    for brand_id, brand_name in list_of_brands.items():

        products = product_api.products(brand=brand_id)

        assert products.data, \
            f"No products returned for brand_id={brand_id}"

        for product in products.data:

            assert product.brand.id == brand_id, \
                (
                    f"Brand ID mismatch: "
                    f"expected={brand_id}, "
                    f"actual={product.brand.id}"
                )

            assert product.brand.name == brand_name, \
                (
                    f"Brand name mismatch: "
                    f"expected={brand_name}, "
                    f"actual={product.brand.name}"
                )


def test_products_have_valid_data(product_api):

    products = product_api.products()

    for product in products.data:

        assert isinstance(product.id, str)
        assert product.id

        assert product.name

        if product.description is not None:
            assert product.description

        assert product.price >= 0

        if product.in_stock is not None:
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


def test_products_with_auth_token(
    product_api,
    auth_token
):

    product_api.client.set_token(auth_token)

    products = product_api.products()

    for product in products.data:

        assert isinstance(product.id, str)
        assert product.id

        assert product.name

        if product.description is not None:
            assert product.description

        assert product.price >= 0


def test_comparing_products_and_product_api_by_id(product_api):

    first_page = product_api.products()

    for page in range(1, first_page.last_page + 1):

        products = product_api.products(page=page)

        for product_data in products.data:

            product_id = product_data.id

            product_by_id = product_api.product_by_id(product_id)

            ResponseValidator.assert_models_equal(
                product_data,
                product_by_id
            )