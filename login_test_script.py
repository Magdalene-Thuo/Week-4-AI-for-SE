from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Setup
driver = webdriver.Chrome()
driver.get("https://example-login.com")  # Replace with real URL

# Test with valid credentials
driver.find_element(By.ID, "username").send_keys("valid_user")
driver.find_element(By.ID, "password").send_keys("valid_pass")
driver.find_element(By.ID, "login-button").click()
time.sleep(2)

if "Dashboard" in driver.page_source:
    print("Valid login test passed")
else:
    print("Valid login test failed")

driver.get("https://example-login.com")

# Test with invalid credentials
driver.find_element(By.ID, "username").send_keys("wrong_user")
driver.find_element(By.ID, "password").send_keys("wrong_pass")
driver.find_element(By.ID, "login-button").click()
time.sleep(2)

if "Invalid credentials" in driver.page_source:
    print("Invalid login test passed")
else:
    print("Invalid login test failed")

driver.quit()

