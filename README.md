# AttendX-Test-Scripts

Automation test scripts for **AttendX**, a student attendance application.
Scripts are written in Python using **Selenium WebDriver** and **pytest**.

## Test Scripts

| File | Purpose | Test Cases |
|------|---------|------------|
| `tests/test_login.py` | Verifies the login module | TC_LOGIN_01 valid login, TC_LOGIN_02 invalid password, TC_LOGIN_03 empty fields |
| `tests/test_mark_attendance.py` | Verifies attendance marking | TC_ATT_01 mark one student present, TC_ATT_02 mark all present |

## How to Run

```bash
pip install selenium pytest
pytest tests/ -v
```

The app is expected to run at `http://localhost:3000`.

## Team Workflow

All QA engineers pull the latest changes before starting work, commit with
clear messages, and push to GitHub instead of sharing files over email or pen drives.

## Contributors

- QA Engineer 1 - Login module tests
- QA Engineer 2 - Attendance module tests
- QA Engineer 3 - Reports module tests (upcoming)
