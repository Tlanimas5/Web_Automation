import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(100)
    yield driver
    driver.quit()


# Select driver and set destination url
def test_login(driver):
    driver.get("https://in.ebay.com/")

    # Verify Landing page is Valid
    try:
        # Is the Page Title Correct?
        assert "Electronics, Cars, Fashion, Collectibles & More | eBay" in driver.title
        print("Home Title is valid")
    except AssertionError:
        print("title not retrieved")

    # Set a wait period for the driver
    wait = WebDriverWait(driver, 10)

    # Navigate to the Client Login Page
    login_page = driver.find_element_by_xpath("//a[@class='nav-link text-white pl-md-4']")
    login_page.click()

    try:
        element = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, '//*[@id="loginModal"]/div/div/div[2]/div[2]/div/div[2]/a/i'))
        )
        print("Client Div element found")
    except TimeoutError:
        print("Element not found")
        driver.quit()

    client_page = driver.find_element_by_xpath('//*[@id="loginModal"]/div/div/div[2]/div[2]/div/div[2]/a/i')
    driver.execute_script("arguments[0].click();", client_page)

    # Is the Page Title Valid for the SignIn?
    try:
        assert "Signin" in driver.title
        title1 = driver.title
        print("Client Sign In Page Reached, Current title is" + title1)
    except AssertionError:
        title1 = driver.title
        print("Not on Client Login Page, where the Title is - " + title1)

    # Login with Valid Credentials
    try:
        wait.until(ec.presence_of_element_located((By.ID, "loginform-email")))
        print("Email field found")
    except TimeoutError:
        print("Email field not found")

    email = driver.find_element_by_id("loginform-email")
    email.send_keys("dwater90@mailinator.com")
    password = driver.find_element_by_id("loginform-password")
    password.send_keys("123")
    driver.find_element_by_name("login-button").send_keys(Keys.ENTER)

    try:
        # assert wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "job-team__user-avatar")))
        wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "job-team__user-avatar")))
        print("Avatar was located")
    except TimeoutError:
        print("Avatar not located")

    try:
        assert "Dashboard – Design Matchup" in driver.title
        title = driver.title
        print("Title is " + title)
    except AssertionError:
        print("Title not found when logged in")