from components.start_inserted_payment import StartInsertedPaymentComponent
from components.component_menu import MenuComponent
from components.login_component import LoginComponent
from components.billing_address_component import BillingAddressComponent
from playwright.sync_api import Page

class CheckoutPage:

    def __init__(self, page: Page):
        self.page = page
        self.menu = MenuComponent(page)
        self.start_inserted_component = StartInsertedPaymentComponent(page)
        self.login_component = LoginComponent(page)
        self.billing_address_component = BillingAddressComponent(page)
