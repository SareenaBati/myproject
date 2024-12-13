#contact me page
from selenium.webdriver.common.by import By

class ContactMe:
    def __init__(self,driver):
        self.driver=driver
        self.Your_Name_textbox=(By.XPATH,"//input[@id='name']")
        self.Your_Email_textbox=(By.XPATH,"//input[@id='email']")
        self.Message_textarea=(By.XPATH,"//textarea[@id='message']")
        self.Submit_button=(By.XPATH,"//button[normalize-space()='Send Message']")

    def open_page(self,url):
        self.driver.get(url)

    def enter_Your_Name(self, Name):
        self.driver.find_element(*self.Your_Name_textbox).send_keys(Name)

    def enter_Your_Email(self, Email):
        self.driver.find_element(*self.Your_Email_textbox).send_keys(Email)

    def enter_Message(self, Message):
        self.driver.find_element(*self.Message_textarea).send_keys(Message)

    def click_submit_button(self):
        self.driver.find_element(*self.Submit_button).click()

