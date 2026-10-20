from playwright.sync_api import Page
from components.component_menu import MenuComponent

class AdminDashboardPage():
    def __init__(self, page: Page):
        self.page = page
        self.menu = MenuComponent(page)