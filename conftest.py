import pytest
from playwright.sync_api import sync_playwright


from pages.login_page import LoginPage
from pages.add_task_page import AddTaskPage
from utils.utils import USER_EMAIL, USER_PASSWORD
from utils.api import TodoistAPIClient


@pytest.fixture(scope="session")
def playwright_browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        yield browser
        browser.close()

@pytest.fixture
def page(playwright_browser):
    context = playwright_browser.new_context()
    page = context.new_page()
    yield page
    context.close()


@pytest.fixture
def login_page(page):
    login = LoginPage(page)
    login.navigate()
    login.login(USER_EMAIL, USER_PASSWORD)
    return login

@pytest.fixture
def add_task_page(page, task_title_fixture, login_page):

    add_task = AddTaskPage(
        page,
        title=task_title_fixture,
        description=task_title_fixture
    )
    add_task.navigate()

    yield add_task

    # remove task after test
    client = TodoistAPIClient()
    tasks = client.get_all_tasks()
    for task in tasks:
        if task["content"].startswith("TASK_"):
            client.delete_task(task["id"])

@pytest.fixture
def task_title_fixture():
    import random
    task_title = f"TASK_{random.randint(0, 99)}"
    yield task_title
