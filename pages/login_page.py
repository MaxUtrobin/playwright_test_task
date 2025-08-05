from playwright.sync_api import Page, expect

from locators.locators import CREATE_TASK_BUTTON
from utils.utils import BASE_URL


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.email_input = page.locator('input[type="email"]')
        self.password_input = page.locator('input[type="password"]')
        self.login_button = page.locator('button[type="submit"]')

    def navigate(self):
        self.page.goto(f"{BASE_URL}/auth/login")

    def login(self, email: str, password: str):
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()

        expect(self.page.locator(CREATE_TASK_BUTTON)).to_be_visible()
