import os

BASE_URL = os.getenv("BASE_URL", "https://app.todoist.com")
TODOIST_API_BASE = os.getenv("TODOIST_API_BASE", "https://api.todoist.com/rest/v2")

USER_EMAIL = os.getenv("USER_EMAIL", "")
USER_PASSWORD = os.getenv("USER_PASSWORD", "")

if not USER_EMAIL or not USER_PASSWORD:
    raise RuntimeError(
        "Please set USER_EMAIL and USER_PASSWORD before running tests:\n"
        '  export USER_EMAIL="your.email@example.com"\n'
        '  export USER_PASSWORD="supersecret"\n'
    )
