from playwright.sync_api import Playwright
from pages.login_page import LoginPage

import pytest

@pytest.fixture(scope="session", autouse=True)
def configure_test_id(playwright: Playwright):
    playwright.selectors.set_test_id_attribute("data-test")

@pytest.fixture
def login_page(page):
    return LoginPage(page)