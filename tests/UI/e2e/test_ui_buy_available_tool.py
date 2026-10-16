import pytest
from playwright.sync_api import expect

@pytest.mark.ui
@pytest.mark.regression
@pytest.mark.smoke
def test_ui_buy_available_tool(home_page, product_details_page, checkout_page):
    home_page.open()
    home_page.first_product_card.click()
    product_details_page.select_add_to_cart()
    product_details_page.menu.cart.is_visible()
    product_details_page.menu.cart.click()
    checkout_page.start_inserted_component.select_proceed_to_checkout_button()
    checkout_page.login_component.login()
    checkout_page.login_component.select_proceed_to_checkout()
    checkout_page.billing_address_component.fill_address()
    checkout_page.billing_address_component.select_payment_method("cash-on-delivery")
    expect(checkout_page.billing_address_component.payment_msg,
           "Payment is failed").to_have_text("Payment was successful")



    


    