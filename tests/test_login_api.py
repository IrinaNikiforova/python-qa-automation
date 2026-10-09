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
    "email,password,status_code,error_msg",
    [
        (USER1["email"], "wrong_password", 401, 'Unauthorized'),
        ("wrong@test.com", USER1["password"], 401, 'Unauthorized'),
        (USER1["email"], "", 401, 'Invalid login request'),
        ("", USER1["password"], 401, 'Invalid login request'),
    ]
)
def test_login_invalid_credentials(auth_api, email, password, status_code, error_msg):

    with pytest.raises(ApiError) as exc_info:
        auth_api.login(email, password)
    
    assert exc_info.value.status_code == status_code, f"status code if frong for : {email} and {password}. Expected: {status_code}. Actual: {exc_info.value.status_code}"
    assert exc_info.value.response_body["error"] == error_msg, f"Expected error msg {error_msg} and actual error msg is {exc_info.value.response_body["error"]}"