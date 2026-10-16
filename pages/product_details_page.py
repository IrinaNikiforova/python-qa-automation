from playwright.sync_api import Page, expect

from components.component_menu import MenuComponent
from config.settings import UI_BASE_URL

class ProductDetailsPage():
    def __init__(self, page:Page):
        self.page = page
        self.menu = MenuComponent(page)
        self.add_to_cart_button = self.page.get_by_test_id("add-to-cart")
        self.out_of_stock_txt = self.page.get_by_test_id("out-of-stock")

    def select_add_to_cart(self):
        self.add_to_cart_button.is_visible()
        self.add_to_cart_button.click()
        