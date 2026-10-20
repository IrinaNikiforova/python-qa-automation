import pytest
from playwright.sync_api import expect
from config.users import ADMIN

@pytest.mark.ui
@pytest.mark.regression
@pytest.mark.smoke
def test_ui_create_new_product(login_page,  admin_dashbourd_page, admin_products_page, admin_products_add_page,new_product_data):
    login_page.open()
    login_page.login(ADMIN["email"],ADMIN["password"])
    admin_dashbourd_page.menu.admin_selects_products()
    admin_products_page.select_add_new_product()
    admin_products_add_page.fill_new_product_fields(new_product_data)
    admin_products_add_page.save_button.click()




    
