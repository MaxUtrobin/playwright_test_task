import pytest
from pages.login_page import LoginPage
from utils.utils import USER_EMAIL, USER_PASSWORD


@pytest.fixture
def login_page(page):
    login = LoginPage(page)
    login.navigate()
    login.login(USER_EMAIL, USER_PASSWORD)
    return login
