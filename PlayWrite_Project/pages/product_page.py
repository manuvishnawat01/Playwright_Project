# pages/product_page.py
# Page Object for Product Details Page.

from playwright.sync_api import expect

class ProductPage:

    def __init__(self, page):
        self.page = page
        self.product_name = page.locator(".product-information h2")
        self.add_to_cart_button = page.locator("button.cart")
        self.view_cart_link = page.locator("#cartModal a[href='/view_cart']")

    def get_product_name(self):
        expect(self.product_name).to_be_visible()
        return self.product_name.inner_text().strip()

    def add_to_cart(self):
        expect(self.add_to_cart_button).to_be_visible()
        self.add_to_cart_button.click()

    def open_cart(self):
        expect(self.view_cart_link).to_be_visible()
        self.view_cart_link.click()
