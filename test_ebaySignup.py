import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver import ActionChains
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
    wait = WebDriverWait(driver, 100)

    # Navigate to the Client Login Page
    my_ebay_link = driver.find_element_by_xpath("//a[@class='gh-eb-li-a'][contains(text(),'My eBay')]")

    # actionChains = ActionChains(driver)

    hover = ActionChains(driver).move_to_element(my_ebay_link)
    hover.perform()

    my_ebay_link.click()

    try:
        assert wait.until(ec.presence_of_all_elements_located((By.ID, 'userid')))
        print("Email/Username is not present")

    except AssertionError:
        print("Element not found")
        driver.quit()

    signup_page = driver.find_element_by_id('InLineCreateAnAccount')
    signup_page.click()
    # driver.execute_script("arguments[0].click();", signup_page)

    # Is the Page Title Valid for the SignIn?
    try:
        assert "Sign in or Register | eBay" in driver.title
        title1 = driver.title
        print("Client Sign In Page Reached, Current title is" + title1)
    except AssertionError:
        title1 = driver.title
        print("Not on Client Login Page, where the Title is - " + title1)

    # Login with Valid Credentials
    try:
        wait.until(ec.presence_of_element_located((By.ID, "firstname")))
        print("First Name field found")
    except TimeoutError:
        print("Email field not found")

    first_name = driver.find_element_by_name("firstname")
    first_name.send_keys("Daniel")
    last_name = driver.find_element_by_id("lastname")
    last_name.send_keys("Flowers")
    email = driver.find_element_by_xpath("//input[@id='email']")
    email.send_keys("dwaters205@qa.com")
    password = driver.find_element_by_name("PASSWORD")
    password.send_keys("Pass@word1")
    submit = driver.find_element_by_id("ppaFormSbtBtn")
    wait.until(ec.element_to_be_selected(submit))
    driver.execute_script("arguments[0].click();", submit)

    try:
        # assert wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "job-team__user-avatar")))
        wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "more")))
        print("DIV was located")
    except TimeoutError:
        print("Avatar not located")

    try:
        assert "My eBay Summary" in driver.title
        title = driver.title
        print("Title is " + title)
    except AssertionError:
        print("Title not found when logged in"+title)
