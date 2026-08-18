import pytest

from api.api_client import ApiClient
from api.auth_api import AuthApi
from exceptions.api_error import ApiError
from config.users import USER1

def test_login(auth_api):

    response = auth_api.login(
        USER1["email"],
        USER1["password"]
    )

    assert response.access_token
    assert response.token_type == "bearer"
    assert response.expires_in > 0


@pytest.mark.parametrize(
    "email,password",
    [
        (USER1["email"], "wrong_password"),
        ("wrong@test.com", USER1["password"]),
        (USER1["email"], ""),
        ("", USER1["password"]),
    ]
)
def test_login_invalid_credentials(auth_api, email, password):

    with pytest.raises(ApiError):
        auth_api.login(email, password)