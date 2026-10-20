from playwright.sync_api import Playwright
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.product_details_page import ProductDetailsPage
from pages.checkout_page import CheckoutPage
from pages.admin_dashboard_page import AdminDashboardPage
from pages.admin_products_page import AdminProductsPage
from pages.admin_products_add_page import AdminProductsAddPage
from helpers.ui_new_product_generator import UINewProductGenerator

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

@pytest.fixture
def admin_dashbourd_page(page):
    return AdminDashboardPage(page)

@pytest.fixture
def admin_products_page(page):
    return AdminProductsPage(page)

@pytest.fixture
def admin_products_add_page(page):
    return AdminProductsAddPage(page)

@pytest.fixture
def new_product_data(images_api, brands_api, categories_api):
    return UINewProductGenerator.generate_product_data_for_ui(
        images_api=images_api,
        brands_api=brands_api,
        categories_api=categories_api,
    )


