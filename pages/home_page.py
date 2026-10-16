from playwright.sync_api import Page, expect

from components.component_menu import MenuComponent
from config.settings import UI_BASE_URL


class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.menu = MenuComponent(page)
        self.product_names = page.get_by_test_id("product-name")
        self.product_cards = page.locator('a.card[data-test^="product-"]')
        self.first_product_card = self.product_cards.first
        self.pagination = page.locator("ul.pagination")
        self.page_buttons = self.pagination.locator('button[aria-label^="Page-"]')
        self.active_page_button = self.pagination.locator("li.active button")
        self.out_of_stock_first_tool = self.product_cards.filter(
            has=page.get_by_test_id("out-of-stock")
        ).first

    def open(self):
        self.page.goto(UI_BASE_URL)

    def get_pages_count(self) -> int:
        expect(self.page_buttons.first).to_be_visible()
        return self.page_buttons.count()

    def select_page_by_number(self, page_number: int):
        expect(self.active_page_button).to_be_visible()
        expect(self.first_product_card).to_be_visible()

        page_label = f"Page-{page_number}"

        if (self.active_page_button.get_attribute("aria-label")== page_label):
            return

        previous_product_id = (self.first_product_card.get_attribute("data-test"))
        assert previous_product_id is not None
       
        button = self.pagination.get_by_role("button", name=page_label, exact=True,)
        button.click()

        expect(self.active_page_button).to_have_attribute("aria-label", page_label, )
        expect(self.first_product_card).not_to_have_attribute("data-test", previous_product_id, )
        expect(self.product_names.first).to_be_visible()

    def get_products_names(self) -> list[str]:
        all_names = []

        expect(self.product_names.first).to_be_visible()
        pages_count = self.get_pages_count()

        for page_number in range(1, pages_count + 1):
            self.select_page_by_number(page_number)

            names = self.product_names.all_text_contents()
            all_names.extend(name.strip() for name in names)

        return all_names

    def select_out_of_stock_tool(self):
        count_of_pages = self.get_pages_count()

        for page_number in range(1, count_of_pages + 1):
            self.select_page_by_number(page_number)

            if self.out_of_stock_first_tool.is_visible():
                self.out_of_stock_first_tool.click()
                return True

        return False

    def select_first_tool(self):
        if self.first_product_card.is_visible:
            self.first_product_card.click()
        raise ValueError("No visible cart on home page")
        