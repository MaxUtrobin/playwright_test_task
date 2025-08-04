# playwright_test_task

Clone project:
- git clone git@github.com:MaxUtrobin/playwright_test_task.git

Create and activate virtual environment
- cd playwright_test_task
- python3 -m venv venv

- source venv/bin/activate 

Install all dependencies: 
- pip install -r requirements.txt

In case of error with pip, try: `pip install --upgrade pip`
 
- playwright install

Set your user email and password:
- export USER_EMAIL="your.email@example.com"
- export USER_PASSWORD="your_password"

Run all tests:

- python -m pytest -v -s