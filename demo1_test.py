#locator
import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeServices
from webdriver_manager.chrome import ChromeDriverManager
import time

from Selenium.code1 import driver


def test_google_search():
    driver=webdriver.Chrome(service=ChromeServices(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.get("https://www.google.com/")
    search_box=driver.find_element(*(By.XPATH,"//textarea[@id='APjFqb']"))
    search_box.send_keys("mindrisers.com.np")
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)

    #search and click on the link
    first_link=driver.find_element(*(By.XPATH,"//h3[contains(text(),'Best IT Training Institute in kathmandu, Nepal | M')]"))
    first_link.click()
    driver.maximize_window()
    time.sleep(5)

    print("congrats!!pytest execute successfully")

