from playwright.sync_api import Playwright
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.product_details_page import ProductDetailsPage
from pages.checkout_page import CheckoutPage

import pytest

@pytest.fixture(scope="session", autouse=True)
def configure_test_id(playwright: Playwright):
    playwright.selectors.set_test_id_attribute("data-test")

@pytest.fixture
def login_page(page):
    return LoginPage(page)

@pytest.fixture
def home_page(page):
    return HomePage(page)

@pytest.fixture
def product_details_page(page):
    return ProductDetailsPage(page)

@pytest.fixture
def checkout_page(page):
    return CheckoutPage(page)