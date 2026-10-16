import pytest
from playwright.sync_api import expect

@pytest.mark.ui
@pytest.mark.regression
@pytest.mark.smoke
def test_ui_buy(home_page, product_details_page):
    
    home_page.open()
    found = home_page.select_out_of_stock_tool()
    assert found, "No out-of-stock product found on any page"

    expect(
        product_details_page.out_of_stock_txt,
        "Expected the product to be out of stock",
    ).to_be_visible()

    expect(
        product_details_page.add_to_cart_button, 
        "Add to card is anable",
    ).to_be_disabled()