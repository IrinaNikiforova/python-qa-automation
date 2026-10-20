from playwright.sync_api import Page

class MenuComponent:
    def __init__(self, page: Page):
        self.page = page

        self.home = page.get_by_test_id("nav-home")
        self.categories = page.get_by_test_id("nav-categories")
        self.contact = page.get_by_test_id("nav-contact")
        self.sign_in = page.get_by_test_id("nav-sign-in")
        self.language_switcher = page.get_by_test_id("language-select")
        self.hand_tools = page.get_by_test_id("nav-hand-tools")
        self.power_tools = page.get_by_test_id("nav-power-tools")
        self.other = page.get_by_test_id("nav-other")
        self.special_tools = page.get_by_test_id("nav-special-tools")
        self.rentals = page.get_by_test_id("nav-rentals")
        self.cart = page.get_by_test_id("nav-cart")
        self.admin_name = page.get_by_test_id("nav-menu")
        self.admin_products = page.get_by_test_id("nav-admin-products")
    
    def back_to_home_page(self):
        self.home.click()

    def select_hand_tools(self):
        self.categories.click()
        self.hand_tools.click()

    def admin_selects_products(self):
        self.admin_name.click()
        self.admin_products.click()
