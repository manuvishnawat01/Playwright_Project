# tests/test_complete_flow.py
# Test 2: Complete End-to-End automation test with milestone screenshots in flat screenshots/ folder.

import os
import config
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

def test_complete_e2e_flow(page):
    os.makedirs("screenshots", exist_ok=True)

    # Initialize Page Objects
    login_page = LoginPage(page)
    home_page = HomePage(page)
    product_page = ProductPage(page)
    cart_page = CartPage(page)

    # Step 1 & 2: Launch website & open login page
    login_page.navigate(config.BASE_URL)
    assert login_page.is_login_page_displayed()
    page.screenshot(path="screenshots/01_website_launched.png")

    # Step 3, 4, 5 & 6: Login & verify success
    login_page.login(config.STANDARD_USER, config.PASSWORD)
    assert home_page.is_logged_in()
    page.screenshot(path="screenshots/02_login_success.png")

    # Step 7: Search for product
    home_page.search_product(config.PRODUCT_NAME)
    page.screenshot(path="screenshots/03_product_searched.png")

    # Step 8 & 9: Open product & add to cart
    home_page.select_first_product()
    assert config.PRODUCT_NAME.lower() in product_page.get_product_name().lower()
    product_page.add_to_cart()
    page.screenshot(path="screenshots/04_product_added_to_cart.png")

    # Step 10 & 11: Open cart & verify product details
    product_page.open_cart()
    assert cart_page.is_cart_page_displayed()
    cart_page.verify_product_in_cart(config.PRODUCT_NAME)
    page.screenshot(path="screenshots/05_cart_opened.png")

    # Step 12 & 13: Logout & verify logout
    cart_page.logout()
    assert login_page.is_login_page_displayed()
    page.screenshot(path="screenshots/06_logout.png")

    print("SUCCESS: Complete E2E flow passed with flat screenshots!")
