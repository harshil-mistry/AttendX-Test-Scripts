"""
AttendX - Login Test Script
Automates the login flow of the AttendX student attendance app using Selenium + pytest.
"""
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "http://localhost:3000"


@pytest.fixture
def driver():
    drv = webdriver.Chrome()
    drv.maximize_window()
    yield drv
    drv.quit()


def login(driver, username, password):
    driver.get(f"{BASE_URL}/login")
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-btn").click()


def test_valid_login(driver):
    """TC_LOGIN_01: Valid teacher credentials should open the dashboard."""
    login(driver, "teacher01", "Pass@123")
    WebDriverWait(driver, 10).until(EC.url_contains("/dashboard"))
    assert "Dashboard" in driver.title


def test_invalid_login(driver):
    """TC_LOGIN_02: Wrong password should show an error message."""
    login(driver, "teacher01", "wrongpass")
    error = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "error-msg"))
    )
    assert "Invalid username or password" in error.text


def test_empty_fields(driver):
    """TC_LOGIN_03: Empty fields should show a validation message."""
    login(driver, "", "")
    error = driver.find_element(By.ID, "error-msg")
    assert "required" in error.text.lower()


def test_logout(driver):
    """TC_LOGIN_04: Logout should return the user to the login page."""
    login(driver, "teacher01", "Pass@123")
    WebDriverWait(driver, 10).until(EC.url_contains("/dashboard"))
    driver.find_element(By.ID, "logout-btn").click()
    WebDriverWait(driver, 10).until(EC.url_contains("/login"))
    assert driver.find_element(By.ID, "login-btn").is_displayed()
