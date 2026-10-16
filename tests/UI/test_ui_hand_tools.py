import pytest
from playwright.sync_api import expect

from config.settings import UI_BASE_URL

@pytest.mark.ui
@pytest.mark.regression
@pytest.mark.smoke
def test_navigation_to_hand_tools_by_menu(home_page, product_api):
    
    home_page.open()
    home_page.menu.select_hand_tools()
    tool_names_from_ui = home_page.get_products_names()
    print("Name of tools: ",tool_names_from_ui)

    page_count_api = product_api.products(category = "hand-tools")
    print("response api: ", page_count_api)
    print("count of pages: ", page_count_api.last_page)
    tool_names_from_api = []
    


