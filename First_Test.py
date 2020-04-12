from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://3.134.118.23/")
assert "Yahoo Mail" in driver.title

print("Title is Yahoo Mail")
Sign_In = driver.find_element_by_id("signin-main")
driver.implicitly_wait(1000)
#print("element q found")
#driver.implicitly_wait(600)
Sign_In.clear()
print("element cleared")
elem = driver.find_element_by_name("btnK")
elem.send_keys("python")
driver.implicitly_wait(3000)
print("pycon was sent to the element")
driver.implicitly_wait(3000)
elem.click()
print("button was clicked")
#elem.send_keys(Keys.RETURN)
driver.implicitly_wait(6000)
#assert "No results found." not in driver.page_source
#driver.implicitly_wait(600)
#driver.quit()