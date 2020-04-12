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
    sign_in = driver.find_element_by_xpath("//*[@id='gh-ug']/a")

    # actionChains = ActionChains(driver)

    hover = ActionChains(driver).move_to_element(sign_in)
    hover.perform()

    sign_in.click()

    try:
        assert wait.until(ec.presence_of_all_elements_located((By.ID, 'userid')))
        print("Email/Username is not present")

    except AssertionError:
        print("Element not found")
        driver.quit()


    # Is the Page Title Valid for the SignIn?
    try:
        assert "Sign in or Register | eBay" in driver.title
        title1 = driver.title
        print("Client Sign In Page Reached, Current title is" + title1)
    except AssertionError:
        title1 = driver.title
        print("Not on Client Login Page, where the Title is - " + title1)

    # Login with Valid Credentials

    userid = driver.find_element_by_name("userid")
    userid.send_keys("hajj3003@qa.team")
    password = driver.find_element_by_id("pass")
    password.send_keys("Pass@word1")
    submit = driver.find_element_by_id("sgnBt")
    # wait.until(ec.element_to_be_selected(submit))
    driver.execute_script("arguments[0].click();", submit)

    try:
        assert wait.until(ec.visibility_of_element_located((By.ID, "gh-ac")))
        print("Search Field Present")
    except AssertionError:
        print("Search Field NOT Present")

    search = driver.find_element_by_id("gh-ac")
    search.send_keys("Pivot table")

    try:
        assert wait.until(ec.visibility_of_element_located((By.ID, "gh-btn")))
        print("Search Button Present")
    except AssertionError:
        print("Search Button NOT Present")

    search_btn = driver.find_element_by_id("gh-btn")
    driver.execute_script("arguments[0].click();", search_btn)

    try:
        assert "Pivot table | eBay" in driver.title
        title = driver.title
        print("Title is " + title)
    except AssertionError:
        print("Title not found when logged in"+title)

    # wait.until(ec.element_to_be_selected((By.XPATH, "//*[@id='srp-river-results-listing3']/div/div[2]/div[4]/div[1]/span")))
    third_item = driver.find_element_by_xpath("//*[@id='srp-river-results-listing3']/div/div[2]/div[3]/div[1]/span")
    print(third_item.text)
    driver.quit()
