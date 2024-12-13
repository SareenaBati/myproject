import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from Selenium.pom.pages.login_page import LoginPage
from Selenium.pom.pages.dashboard_page import  DashboardPage
from Selenium.pom.pages.aboutyourself_page import AboutYourSelfPage
from Selenium.pom.pages.article_page import ArticlePage
from Selenium.pom.pages.contactme_page import ContactMe
from Selenium.pom.pages.qatesting_page import QATesting
from Selenium.pom.pages.company_page import Company


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_login(driver):
    login_page = LoginPage(driver)
    login_page.open_page("https://sagar-test-qa.vercel.app/")
    driver.maximize_window()

    time.sleep(1)  # Optional: can be removed
    login_page.enter_username("TestQA")
    time.sleep(1)  # Optional: can be removed
    login_page.enter_password("password")
    time.sleep(1)  # Optional: can be removed
    login_page.click_login()
    time.sleep(5)  # Wait for the page to load completely
    print("Page executed successfully!!!!")


@pytest.mark.parametrize("username, password", [
    ("TestQA", "password"),  # Valid username and password
    ("invaliduser", "invalidpass"),  # Invalid username and password
    ("1", "a"),  # Invalid username and password (invalid)
    ("user3", "pass3"),  # Invalid username and password
])
def test_login1(driver, username, password):
    login_page = LoginPage(driver)
    login_page.open_page("https://sagar-test-qa.vercel.app/")

    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()

    alert_text = login_page.get_alert_text_and_accept()  # Ensure this method is implemented in your LoginPage class
    if alert_text and "Invalid username or password" in alert_text:
        print(f"Invalid username or password for {username}")
    else:
        if login_page.is_dashboard_present():  # Ensure this method is implemented in your LoginPage class
            print(f"Login successful for {username}")
        else:
            print(f"Unexpected error or login failed for {username}")

#Redirect to dashboard page...
def test_dashboard_page(driver):
    dashboard_page=DashboardPage(driver)
    dashboard_page.open_dashboard_page("https://sagar-test-qa.vercel.app/dashboard.html")
    driver.maximize_window()
    time.sleep(5)
    print("Dashboard page login successfully")



def test_About_yourself_page(driver):
    aboutyourself_page=AboutYourSelfPage(driver)
    aboutyourself_page.open_page("https://sagar-test-qa.vercel.app/about.html")
    time.sleep(1)
    driver.maximize_window()
    aboutyourself_page.enter_Full_Name("Test")
    time.sleep(1)
    aboutyourself_page.enter_Phone(9874561231)
    time.sleep(1)
    aboutyourself_page.enter_Email("test@gmail.com")
    time.sleep(1)
    aboutyourself_page.enter_Hobby("sleeping")
    time.sleep(1)
    aboutyourself_page.click_submit_button()
    time.sleep(3)



def test_article(driver):
    article=ArticlePage(driver)
    article.open_page("https://sagar-test-qa.vercel.app/articles.html")
    driver.maximize_window()
    time.sleep(10)
    page_height = driver.execute_script("return document.body.scrollHeight")
    scroll_speed = 1
    scroll_iteration = int(page_height / scroll_speed)
    for _ in range(scroll_iteration):
        driver.execute_script(f"window.scrollBy(0,{scroll_speed});")
    time.sleep(2)


def test_contact(driver):
    contactme=ContactMe(driver)
    contactme.open_page("https://sagar-test-qa.vercel.app/contact.html")
    driver.maximize_window()
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(0.5)
    contactme.enter_Your_Name("test")
    time.sleep(1)
    contactme.enter_Your_Email("test@gmail.com")
    time.sleep(1)
    contactme.enter_Message("QA")
    time.sleep(1)
    contactme.click_submit_button()
    time.sleep(3)
    print(f"it work")

def test_qatesting(driver):
    testing=QATesting(driver)
    testing.open_page("https://sagar-test-qa.vercel.app/qa.html")
    driver.maximize_window()
    time.sleep(12)
    page_height = driver.execute_script("return document.body.scrollHeight")
    scroll_speed = 1
    scroll_iteration = int(page_height / scroll_speed)
    for _ in range(scroll_iteration):
        driver.execute_script(f"window.scrollBy(0,{scroll_speed});")
    time.sleep(2)


def test_company(driver):
    company=Company(driver)
    company.open_page("https://sagar-test-qa.vercel.app/company.html")
    driver.maximize_window()
    time.sleep(10)
    page_height=driver.execute_script("return document.body.scrollHeight")
    scroll_speed=1
    scroll_iteration=int(page_height/scroll_speed)
    for _ in range(scroll_iteration):
        driver.execute_script(f"window.scrollBy(0,{scroll_speed});")
    time.sleep(2)











