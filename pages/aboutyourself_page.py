#about yourself
from selenium.webdriver.common.by import  By

class AboutYourSelfPage:
    def __init__(self,driver):
        self.driver=driver
        self.Full_Name_textbox=(By.XPATH,"//input[@id='fullname']")
        self.Phone_textbox = (By.XPATH, "//input[@id='phone']")
        self.Email_textbox = (By.XPATH, "//input[@id='email']")
        self.Hobby_textbox = (By.XPATH, "//input[@id='hobby']")
        self.Submit_button=(By.XPATH,"//button[normalize-space()='Submit']")

    def open_page(self,url):
        self.driver.get(url)

    def enter_Full_Name(self, Name):
        self.driver.find_element(*self.Full_Name_textbox).send_keys(Name)

    def enter_Phone(self,Phone):
        self.driver.find_element(*self.Phone_textbox).send_keys(Phone)

    def enter_Email(self,Email):
        self.driver.find_element(*self.Email_textbox).send_keys(Email)

    def enter_Hobby(self,Hobby):
        self.driver.find_element(*self.Hobby_textbox).send_keys(Hobby)


    def click_submit_button(self):
        self.driver.find_element(*self.Submit_button).click()





