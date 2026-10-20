from playwright.sync_api import Page
from components.component_menu import MenuComponent
from helpers.ui_new_product_generator import UINewProductGenerator

class AdminProductsAddPage():
    
    def __init__(self, page: Page):
        self.page = page
        self.menu = MenuComponent(page)
        self.name = page.get_by_test_id("name")
        self.description = page.get_by_test_id("description")
        self.stock = page.get_by_test_id("stock")
        self.stock = page.get_by_test_id("stock")
        self.price = page.get_by_test_id("price")
        self.location_offer_checkbox = page.get_by_test_id("location-offer")
        self.item_for_rent_checkbox = page.get_by_test_id("rental")
        self.co2_rating_dropdown = page.get_by_test_id("co2-rating")
        self.brand_id_dropdown = page.get_by_test_id("brand-id")
        self.category_id_dropdown = page.get_by_test_id("category-id")
        self.image_dropdown = page.get_by_test_id("product-image-id")
        self.save_button = page.get_by_test_id("product-submit")

    def fill_new_product_fields(self, payload: dict):
        print(payload)
        self.name.fill(payload["name"])
        self.description.fill(payload["description"])
        self.stock.fill(payload["stock"])
        self.price.fill(payload["price"])
        self.location_offer_checkbox.check()
        self.item_for_rent_checkbox.check()
        self.brand_id_dropdown.select_option(value=payload["brand"])
        self.category_id_dropdown.select_option(value=payload["category"])
        self.image_dropdown.select_option(value=payload["image"])
        

        
