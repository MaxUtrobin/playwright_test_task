from playwright.sync_api import Page

from utils.utils import BASE_URL
from locators.locators import CREATE_TASK_BUTTON, ADD_TASK_TITLE, ADD_TASK_DESCRIPTION, PRIORITY_OPTION, SELECT_TASK, \
    PRIORITY_BUTTON, SAVE_TASK_BUTTON


class AddTaskPage:
    def __init__(self, page: Page, title, description, priority=1, task_date=""):
        self.page = page

        self.title = title
        self.description = description
        self.priority = priority
        self.task_date = task_date

    def navigate(self):
        self.page.goto(f"{BASE_URL}/app/inbox")

    def click_add_task(self):
        self.page.locator(CREATE_TASK_BUTTON).click()

    def add_task_title(self):
        self.page.locator(ADD_TASK_TITLE).fill(self.title)

    def add_task_description(self):
        self.page.locator(ADD_TASK_DESCRIPTION).fill(self.description)

    def _priority_option(self, level: int):
        return self.page.locator(PRIORITY_OPTION.format(level))

    def add_task_priority(self, priority):
        self.page.locator(PRIORITY_BUTTON).click()
        self._priority_option(priority).click()

    def save_task(self):
        self.page.locator(SAVE_TASK_BUTTON).click()

    def select_task(self, task_name):
        self.page.locator(SELECT_TASK.format(task_name)).click()

    def assert_task_priority(self, task_priority):
        return self.page.locator(f'//div[@aria-label="Priority"]//span[contains(., "P{task_priority}")]')
