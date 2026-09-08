# step_definitions/login_steps.py
# Test Case 1: BDD Step Definitions.

import os
import config
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pytest_bdd import given, when, then, parsers, scenarios

scenarios("../features/login.feature")
active_user = ""

@given("I launch the login page")
def launch_login_page(page):
    login_page = LoginPage(page)
    login_page.navigate(config.BASE_URL)

@when(parsers.parse('I login with email "{email}" and password "{password}"'))
def login_with_credentials(page, email, password):
    global active_user
    active_user = email
    login_page = LoginPage(page)
    login_page.login(email, password)

@then("I should see the logged in user indicator")
def verify_logged_in_user(page):
    home_page = HomePage(page)
    assert home_page.is_logged_in()

    os.makedirs("screenshots/bdd", exist_ok=True)
    user_id = active_user.split("@")[0]
    page.screenshot(path=f"screenshots/bdd/{user_id}_login.png")

@then("I logout from the application")
def logout_application(page):
    home_page = HomePage(page)
    home_page.logout()
    login_page = LoginPage(page)
    assert login_page.is_login_page_displayed()

    os.makedirs("screenshots/bdd", exist_ok=True)
    user_id = active_user.split("@")[0]
    page.screenshot(path=f"screenshots/bdd/{user_id}_logout.png")
