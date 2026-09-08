# pages/cart_page.py
# Page Object for Shopping Cart Page.

from playwright.sync_api import expect

class CartPage:

    def __init__(self, page):
        self.page = page
        self.cart_table = page.locator("#cart_info")
        self.cart_item = page.locator("td.cart_description a")
        self.logout_link = page.locator("a[href='/logout']")

    def is_cart_page_displayed(self):
        expect(self.cart_table).to_be_visible()
        return "view_cart" in self.page.url

    def verify_product_in_cart(self, expected_name):
        expect(self.cart_item.first).to_be_visible()
        actual_name = self.cart_item.first.inner_text().strip()
        assert expected_name.lower() in actual_name.lower()

    def logout(self):
        expect(self.logout_link).to_be_visible()
        self.logout_link.click()
