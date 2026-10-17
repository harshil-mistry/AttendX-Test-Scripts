"""
AttendX - Attendance Marking Test Script
Automates marking student attendance for a class using Selenium + pytest.
"""
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "http://localhost:3000"


@pytest.fixture
def logged_in_driver():
    drv = webdriver.Chrome()
    drv.maximize_window()
    drv.get(f"{BASE_URL}/login")
    drv.find_element(By.ID, "username").send_keys("teacher01")
    drv.find_element(By.ID, "password").send_keys("Pass@123")
    drv.find_element(By.ID, "login-btn").click()
    WebDriverWait(drv, 10).until(EC.url_contains("/dashboard"))
    yield drv
    drv.quit()


def open_attendance_page(driver, class_name):
    driver.get(f"{BASE_URL}/attendance")
    Select(driver.find_element(By.ID, "class-select")).select_by_visible_text(class_name)
    driver.find_element(By.ID, "load-students").click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".student-row"))
    )


def test_mark_student_present(logged_in_driver):
    """TC_ATT_01: Marking a student present should save successfully."""
    driver = logged_in_driver
    open_attendance_page(driver, "SY-IT-A")
    driver.find_element(By.CSS_SELECTOR, "#student-101 .present-radio").click()
    driver.find_element(By.ID, "save-attendance").click()
    toast = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "toast-success"))
    )
    assert "Attendance saved" in toast.text


def test_mark_all_present(logged_in_driver):
    """TC_ATT_02: 'Mark all present' should select present for every student."""
    driver = logged_in_driver
    open_attendance_page(driver, "SY-IT-A")
    driver.find_element(By.ID, "mark-all-present").click()
    radios = driver.find_elements(By.CSS_SELECTOR, ".present-radio")
    assert all(r.is_selected() for r in radios)
