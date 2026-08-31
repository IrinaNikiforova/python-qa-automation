import pytest

from pages.checkout_page import CheckoutPage
from api.api_client import ApiClient
from api.auth_api import AuthApi
from api.product_api import ProductApi
from config.users import USER1, USER2, USER3, ADMIN
from api.user_api import UserApi


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

@pytest.fixture
def auth_api(api_client):
    return AuthApi(api_client)

@pytest.fixture
def product_api(api_client):
    return ProductApi(api_client)

@pytest.fixture
def auth_token(auth_api):
    login_response = auth_api.login(
        USER1["email"],
        USER1["password"]
    )
    return login_response.access_token

@pytest.fixture
def auth_admin_token(auth_api):
    login_response = auth_api.login(
        ADMIN["email"],
        ADMIN["password"]
    )
    return login_response.access_token

@pytest.fixture
def user_api(api_client):
    return UserApi(api_client)