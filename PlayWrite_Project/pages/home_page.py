# pages/home_page.py
# Page Object for Home Page & Header Navigation.

from playwright.sync_api import expect

class HomePage:

    def __init__(self, page):
        self.page = page
        self.logged_in_text = page.locator("a:has-text('Logged in as')")
        self.search_input = page.locator("#search_product")
        self.search_button = page.locator("#submit_search")
        self.logout_link = page.locator("a[href='/logout']")

    def is_logged_in(self):
        expect(self.logged_in_text).to_be_visible()
        return self.logged_in_text.is_visible()

    def search_product(self, product_name):
        self.page.goto("https://automationexercise.com/products")
        expect(self.search_input).to_be_visible()
        self.search_input.fill(product_name)
        self.search_button.click()

    def select_first_product(self):
        view_button = self.page.locator("a[href^='/product_details/']").first
        expect(view_button).to_be_visible()
        href = view_button.get_attribute("href")
        self.page.goto(f"https://automationexercise.com{href}")

    def logout(self):
        expect(self.logout_link).to_be_visible()
        self.logout_link.click()
