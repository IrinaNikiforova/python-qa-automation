class PaymentMethodComponent: 

    def select_credit_card(self):
        print("Credit Card selected")

    def select_cash(self):
        print("Cash selected")


class CheckoutPage:

    def __init__(self):
        self.payment_method = PaymentMethodComponent()

    def checkout(self):
        print("checkout completed")


checkout_page = CheckoutPage()
checkout_page.payment_method.select_credit_card()
checkout_page.checkout()