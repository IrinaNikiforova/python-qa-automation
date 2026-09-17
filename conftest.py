import pytest

from pages.checkout_page import CheckoutPage
from api.api_client import ApiClient
from api.auth_api import AuthApi
from api.product_api import ProductApi
from config.users import USER1, USER2, USER3, ADMIN
from api.user_api import UserApi
from helpers.product_payload_generator import ProductPayloadGenerator


@pytest.fixture
def checkout_page():
    print("SETUP: Creating CheckoutPage")

    page = CheckoutPage()

    yield page

    print("TEARDOWN: Closing CheckoutPage")

@pytest.fixture
def api_client():
    return ApiClient(
        "https://api.practicesoftwaretesting.com"
    )

@pytest.fixture(scope="session")
def auth_api_client():
    return ApiClient("https://api.practicesoftwaretesting.com")

@pytest.fixture(scope="session")
def auth_api(auth_api_client):
    return AuthApi(auth_api_client)

@pytest.fixture
def product_api(api_client):
    return ProductApi(api_client)

@pytest.fixture(scope="session")
def auth_token(auth_api):
    login_response = auth_api.login(
        USER1["email"],
        USER1["password"]
    )
    return login_response.access_token

@pytest.fixture(scope="session")
def auth_admin_token(auth_api):
    login_response = auth_api.login(
        ADMIN["email"],
        ADMIN["password"]
    )
    return login_response.access_token

@pytest.fixture
def user_api(api_client):
    return UserApi(api_client)

@pytest.fixture
def created_product(product_api, auth_admin_token):
    max_retries = 3
    payload = ProductPayloadGenerator.collect_products_data(product_api)
    product_api.client.set_token(auth_admin_token)
    for attempt in range(1, max_retries + 1):
        try:      
            response = product_api.create_product(payload)
            break
        except ApiError as e:
            if e.status_code in (400, 401, 403, 404) or attempt == max_retries:
                raise
    try:
        yield payload, response
    finally:
        product_api.delete_product(response.id)

