import pytest
import random
from pages.add_task_page import AddTaskPage
from utils.api import TodoistAPIClient


@pytest.fixture
def task_title_fixture():
    return f"TASK_{random.randint(0, 99)}"


@pytest.fixture
def add_task_page(page, login_page, task_title_fixture):
    task_page = AddTaskPage(
        page, title=task_title_fixture, description=task_title_fixture
    )
    task_page.navigate()

    yield task_page

    # remove task after test
    client = TodoistAPIClient()
    for task in client.get_all_tasks():
        if task["content"].startswith("TASK_"):
            client.delete_task(task["id"])
