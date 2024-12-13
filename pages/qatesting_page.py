# QA testing
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class QATesting:
    def __init__(self,driver):
        self.driver=driver

    def open_page(self, url):
        self.driver.get(url)



