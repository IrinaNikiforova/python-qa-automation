class BasePage:
    def __init__(self, url):
        self.url = url
    
    def open(self):
        print(f"Opening {self.url}")

class ProductPage(BasePage):
    def __init__(self, url):
        super().__init__(url)

    def open(self):
        print(f"Opening product page {self.url}")

    
    def search_product(self, name):
        print(f"Searching for {name}")

page = ProductPage("https://shop.com")

page.open()
page.search_product("Laptop")
        