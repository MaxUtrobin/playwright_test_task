# playwright_test_task

Create and activate virtual environment
- cd playwright_test_task
- python3 -m venv venv

- source venv/bin/activate 

Install all dependencies: 
- pip install -r requirements.txt

- playwright install

Set your user email and password:
- export USER_EMAIL="your.email@example.com"
- export USER_PASSWORD="your_password"

Run all tests:

- python -m pytest -v -s