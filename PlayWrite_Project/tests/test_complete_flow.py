# tests/test_complete_flow.py
# Test Case 3: Complete End-to-End flow taking screenshots ONLY when each page opens.

import os
import config
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

def test_complete_e2e_flow(page):
    os.makedirs("screenshots/complete_flow", exist_ok=True)

    # Initialize Page Objects
    login_page = LoginPage(page)
    home_page = HomePage(page)
    product_page = ProductPage(page)
    cart_page = CartPage(page)

    # 1. Screenshot when Login Page Opens
    login_page.navigate(config.BASE_URL)
    assert login_page.is_login_page_displayed()
    page.screenshot(path="screenshots/complete_flow/01_login_page.png")

    # 2. Screenshot when Home Page Opens (after login)
    login_page.login(config.STANDARD_USER, config.PASSWORD)
    assert home_page.is_logged_in()
    page.screenshot(path="screenshots/complete_flow/02_home_page.png")

    # Search product & open product page
    home_page.search_product(config.PRODUCT_NAME)
    home_page.select_first_product()
    assert config.PRODUCT_NAME.lower() in product_page.get_product_name().lower()

    # 3. Screenshot when Product Page Opens
    page.screenshot(path="screenshots/complete_flow/03_product_page.png")

    # Add to cart & open cart page
    product_page.add_to_cart()
    product_page.open_cart()
    assert cart_page.is_cart_page_displayed()

    # 4. Screenshot when Cart Page Opens
    cart_page.verify_product_in_cart(config.PRODUCT_NAME)
    page.screenshot(path="screenshots/complete_flow/04_cart_page.png")

    # Logout
    cart_page.logout()
    assert login_page.is_login_page_displayed()
