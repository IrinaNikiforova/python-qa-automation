from playwright.sync_api import Page

class BillingAddressComponent():
    def __init__(self, page: Page):
        self.page = page
        self.coundry_drop_down = self.page.get_by_test_id("country")
        self.postal_code = self.page.get_by_test_id("postal_code")
        self.house_number = self.page.get_by_test_id("house_number")
        self.street = self.page.get_by_test_id("street")
        self.city = self.page.get_by_test_id("city")
        self.state = self.page.get_by_test_id("state")
        self.proceed_to_checkout = self.page.get_by_test_id("proceed-3")
        self.payment_method = self.page.get_by_test_id("payment-method")
        self.check_payment_button = self.page.get_by_test_id("finish")
        self.payment_msg = self.page.get_by_test_id("payment-success-message")

    def fill_address(self):
        self.coundry_drop_down.select_option(label="United States of America (the)")
        self.postal_code.fill("33126")
        self.house_number.fill("3731")
        self.street.fill("NW 2nd")
        self.city.fill("Miami")
        self.state.fill("FL")
        self.proceed_to_checkout.is_enabled()
        self.proceed_to_checkout.click()

    def select_payment_method(self, payment_method: str):
        self.check_payment_button.is_visible()
        self.payment_method.select_option(value=payment_method)
        self.check_payment_button.is_enabled()
        self.check_payment_button.click()






