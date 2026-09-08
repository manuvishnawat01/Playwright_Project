# pages/login_page.py
# Page Object for Login Page.

class LoginPage:

    def __init__(self, page):
        self.page = page
        self.login_heading = page.locator("h2:has-text('Login to your account')")
        self.email_input = page.locator("[data-qa='login-email']")
        self.password_input = page.locator("[data-qa='login-password']")
        self.login_button = page.locator("[data-qa='login-button']")

    def navigate(self, base_url):
        self.page.goto(f"{base_url}/login")

    def login(self, email, password):
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()

    def is_login_page_displayed(self):
        return self.login_heading.is_visible()
