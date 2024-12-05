import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Setup WebDriver
@pytest.fixture
def driver():
    driver = webdriver.Chrome()  # Make sure to update the path if needed
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()

# Positive test: Correct login credentials
def test_positive_login(driver):
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    assert driver.title == "Swag Labs"  # Check the title after login
    sleep(5)

# Negative test: Incorrect login credentials
def test_negative_login(driver):
    driver.find_element(By.ID, "user-name").send_keys("wrong_user")
    driver.find_element(By.ID, "password").send_keys("wrong_password")
    driver.find_element(By.ID, "login-button").click()
    error_message = driver.find_element(By.CSS_SELECTOR, ".error-message-container").text
    assert "Epic sadface" in error_message  # Verify the error message
    print(f"Error message displayed: {error_message}")
    sleep(5)