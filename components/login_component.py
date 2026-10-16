from playwright.sync_api import Page
from config.users import USER1

class LoginComponent():
    def __init__(self, page: Page):
        self.page = page
        self.login_field = self.page.get_by_test_id("email")
        self.password_field = self.page.get_by_test_id("password")
        self.login_button = self.page.get_by_test_id("login-submit")
        self.proceed_to_checkout_button = self.page.get_by_test_id("proceed-2")

    def login(self):        
        self.login_field.fill(USER1["email"])
        self.password_field.fill(USER1["password"])
        self.login_button.is_enabled()
        self.login_button.click()

    def select_proceed_to_checkout(self):
        self.proceed_to_checkout_button.is_visible()
        self.proceed_to_checkout_button.click()

        

    
