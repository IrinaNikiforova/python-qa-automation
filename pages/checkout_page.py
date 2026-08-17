from components.payment_method_component import PaymentMethodComponent


class CheckoutPage:

    def __init__(self):
        print("Creating CheckoutPage")
        self.payment_method = PaymentMethodComponent()

    def checkout(self):
        return "Checkout completed"