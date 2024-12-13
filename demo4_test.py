import time
import re
import random
import string
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Pytest fixture to set up and tear down the WebDriver
@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
# Function to check if a string is a valid email address
def is_valid_email(email):
    email_pattern = "^[a-z]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
    return bool(re.search(email_pattern, email))

# Function to generate random data
def generate_random_email():
    domain = "test.com"
    email_length = 5
    random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(email_length))
    return random_string + "@" + domain

def generate_random_name():
    return ''.join(random.choices(string.ascii_letters, k=6))

def generate_random_phone():
    return "98" + ''.join(random.choices(string.digits, k=8))
# Generate random data for 5 test cases
random_data = [
    (
        generate_random_name(),
        generate_random_email(),
        generate_random_phone()
    )
    for _ in range(2)
]

# Test function to fill the form with random data
@pytest.mark.parametrize("name, email, phone", random_data)
def test_form_filling(driver, name, email, phone):
    driver.get("https://mindrisers.com.np/contact-us")
    driver.maximize_window()

    # Scroll to the form
    target_y = 6000
    scroll_distance = 1000
    current_y = 0

    while current_y < target_y:
        driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
        current_y += scroll_distance
        time.sleep(0.25)
        # Locate form fields and fill them with random data
        name_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Name']"))
        )
        email_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Email']"))
        )
        phone_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Phone']"))
        )

        # Fill the form fields
        name_field.clear()
        name_field.send_keys(name)
        time.sleep(0.75)

        if is_valid_email(email):
            email_field.clear()
            email_field.send_keys(email)
        else:
            print("Invalid email address")
        time.sleep(0.75)

        phone_field.clear()
        phone_field.send_keys(phone)
        time.sleep(0.75)

        # print the value for verification
        print(f"First Name:{name}")
        print(f"Email:{email}")
        print(f"Phone Number:{phone}")