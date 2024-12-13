#login page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_text = (By.XPATH, "//input[@id='username']")
        self.password_textbox = (By.XPATH, "//input[@id='password']")
        self.login_button = (By.XPATH, "//button[normalize-space()='Login']")

    def open_page(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        self.driver.find_element(*self.username_text).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_textbox).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def get_alert_text_and_accept(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            alert.accept()
            return alert_text
        except :
            return None

    def is_dashboard_present(self):
        time.sleep(2)
        return "Welcome to the Dashboard" in self.driver.page_source


