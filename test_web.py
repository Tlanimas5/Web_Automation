import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_basic_duckduckgo_search(browser):
    url = 'https://www.duckduckgo.com'
    phrase = 'panda'

    browser.get(url)

    search_input = browser.find_element_by_id('search_form_input_homepage')
    search_input.send_keys(phrase + Keys.RETURN)

    link_divs = browser.find_elements_by_css_selector('#links > div')
    assert len(link_divs) > 0

    xpath = "//div[@id='links']//*[contains(text(), '{phrase}')]"
    results = browser.find_elements_by_xpath(xpath)
    assert len(results) > 0

    search_input = browser.find_element_by_id('search_form_input')
    assert search_input.get_attribute('value') == phrase
