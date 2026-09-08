# conftest.py
# Pytest fixture for Playwright browser setup and failure screenshots.

import os
import pytest
from playwright.sync_api import sync_playwright

_driver_page = None

@pytest.fixture
def page():
    """Launches Chromium browser in headed mode with slow motion delay."""
    global _driver_page
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1500)
        _driver_page = browser.new_page()
        yield _driver_page
        browser.close()
        _driver_page = None

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Automatically takes a screenshot if any test step fails."""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        if _driver_page:
            os.makedirs("screenshots/failures", exist_ok=True)
            test_name = item.name.replace("[", "_").replace("]", "_")
            _driver_page.screenshot(path=f"screenshots/failures/{test_name}.png")
