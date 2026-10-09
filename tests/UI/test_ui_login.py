import pytest
from playwright.sync_api import expect

from config.settings import UI_BASE_URL
from config.users import USER1, ADMIN

@pytest.mark.parametrize(
    "email, password, role",
    [
        (USER1["email"], USER1["password"], USER1["role"]),
        (ADMIN["email"], ADMIN["password"], ADMIN["role"]),
    ]
)
def test_successful_login(login_page, email, password, role):
    login_page.open()
    login_page.login(email, password)

    if role == "user":
        expect(login_page.page).to_have_url(f"{UI_BASE_URL}/account")
    elif role == "admin":
        expect(login_page.page).to_have_url(
            f"{UI_BASE_URL}/admin/dashboard"
        )
    else:
        raise ValueError(f"Unexpected role: {role}")

@pytest.mark.parametrize(
    "email, password, type_of_error, expected_error_msg",
    [
        (USER1["email"], "", "wrong password", "Password is required"),
        (USER1["email"], "sdffdff", "failed credo", "Invalid email or password"),
        ("", USER1["password"],"wrong email","Email is required"),
        ("dafvdffdsvd", USER1["password"],"wrong email","Email format is invalid"),
        ("dafvdffdsvd@dfvf.com", "1234","failed credo","Invalid email or password"),
    ]
)
def test_failed_login(login_page, email, password, type_of_error, expected_error_msg):
    login_page.open()
    login_page.login(email, password)
    print("Expected Error: ",expected_error_msg)
    error_locator = login_page.get_error_locator(type_of_error)
    print(error_locator)
    expect(error_locator).to_be_visible()
    expect(error_locator).to_have_text(expected_error_msg)