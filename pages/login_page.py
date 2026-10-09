from playwright.sync_api import Page
from config.settings import UI_BASE_URL

class LoginPage:
    def __init__(self, page:Page):
        self.page = page

        self.email_input = page.get_by_test_id("email")
        self.password_input = page.get_by_test_id("password")
        self.login_button = page.get_by_test_id("login-submit")
        self.email_error_message = page.get_by_test_id("email-error") 
        self.password_error_message = page.get_by_test_id("password-error") 
        self.login_error_message = page.get_by_test_id("login-error") 
    
    def open(self):
        self.page.goto(f"{UI_BASE_URL}/auth/login")

    def login(self, email:str, password:str):
        self.fill_email(email)
        self.fill_password(password)
        self.click_login_button()

    def fill_email(self, email: str):
        self.email_input.fill(email)

    def fill_password(self, password: str):
        self.password_input.fill(password)

    def click_login_button(self):
        self.login_button.click()

    def get_error_locator(self, type_of_error: str):
        if type_of_error == "wrong email":
            return self.email_error_message
        if type_of_error == "wrong password":
            return self.password_error_message
        if type_of_error == "failed credo":
            return self.login_error_message

        raise ValueError(f"Unknown error type: {type_of_error}")
    