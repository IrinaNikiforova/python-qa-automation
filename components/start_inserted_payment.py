from playwright.sync_api import Page

class StartInsertedPaymentComponent():
    def __init__(self, page: Page):
        self.page = page
        self.prodeed_to_checkout_start = self.page.get_by_test_id("proceed-1")

    def select_proceed_to_checkout_button(self):
        self.prodeed_to_checkout_start.is_visible()
        self.prodeed_to_checkout_start.click()
        