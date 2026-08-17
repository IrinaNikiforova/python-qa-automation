import pytest

from api.api_client import ApiClient
from api.auth_api import AuthApi
from exceptions.api_error import ApiError

def test_login(auth_api):

    response = auth_api.login(
        "customer@practicesoftwaretesting.com",
        "welcome01"
    )

    assert response.access_token
    assert response.token_type == "bearer"
    assert response.expires_in > 0


@pytest.mark.parametrize(
    "email,password",
    [
        ("customer@practicesoftwaretesting.com", "wrong_password"),
        ("wrong@test.com", "welcome01"),
        ("customer@practicesoftwaretesting.com", ""),
        ("", "welcome01"),
    ]
)
def test_login_invalid_credentials(auth_api, email, password):

    with pytest.raises(ApiError):
        auth_api.login(email, password)