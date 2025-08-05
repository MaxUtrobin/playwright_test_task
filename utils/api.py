import requests

from utils.logger import get_logger
from utils.utils import TODOIST_API_BASE, USER_EMAIL, USER_PASSWORD

logger = get_logger()


class TodoistAPIClient:
    def __init__(self):
        self.email = USER_EMAIL
        self.password = USER_PASSWORD
        self.token = self.get_auth_token()

    def get_auth_token(self):
        logger.info("Getting auth token...")
        url = "https://app.todoist.com/api/v1/user/login"
        payload = {
            "email": self.email,
            "password": self.password,
            "web_session": True,
            "permanent_login": True,
        }
        response = requests.post(url, json=payload)
        response.raise_for_status()
        self.token = response.json()["token"]
        logger.info(f"Token is received, for `{response.json()['email']}` user")
        return self.token

    def get_headers(self):
        return {"Authorization": f"Bearer {self.token}"}

    def get_all_tasks(self):
        logger.info("Getting all tasks...")
        response = requests.get(f"{TODOIST_API_BASE}/tasks", headers=self.get_headers())
        response.raise_for_status()
        return response.json()

    def delete_task(self, task_id):
        logger.info(f"Deleting task {task_id}")
        response = requests.delete(
            f"{TODOIST_API_BASE}/tasks/{task_id}", headers=self.get_headers()
        )
        if response.status_code == 204:
            logger.info(f"Task `{task_id}` is deleted successfully")
        else:
            logger.error(f"Failed to delete task `{task_id}`: {response.status_code}")
