from playwright.sync_api import Page
from components.component_menu import MenuComponent

class AdminProductsPage():
    def __init__(self, page: Page):
        self.page = page
        self.menu = MenuComponent(page)
        self.add_product_button = page.get_by_test_id("product-add")

    def select_add_new_product(self):
        self.add_product_button.click()
        