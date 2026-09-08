# tests/test_data_driven_login.py
# Test Case 2: CSV Data-Driven Login Test using Pytest parameterization.

import os
import pytest
import config
from utils.csv_reader import get_csv_data
from pages.login_page import LoginPage
from pages.home_page import HomePage

login_data = get_csv_data("test_data/login_data.csv")

@pytest.mark.parametrize("username,password", login_data)
def test_csv_data_driven_login(page, username, password):
    os.makedirs("screenshots/data_driven", exist_ok=True)
    user_id = username.split("@")[0]

    login_page = LoginPage(page)
    home_page = HomePage(page)

    # 1. Login
    login_page.navigate(config.BASE_URL)
    login_page.login(username, password)

    # 2. Verify Login & Screenshot
    assert home_page.is_logged_in()
    page.screenshot(path=f"screenshots/data_driven/{user_id}_login.png")

    # 3. Logout & Screenshot
    home_page.logout()
    assert login_page.is_login_page_displayed()
    page.screenshot(path=f"screenshots/data_driven/{user_id}_logout.png")
