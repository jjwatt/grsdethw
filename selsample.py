from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import firefox

ffoptions = firefox.options.Options()
ffoptions.headless = True
driver = webdriver.Firefox(options=ffoptions)
# driver = webdriver.PhantomJS()
# driver = webdriver.Remote("172.26.208.1:4444")
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found" not in driver.page_source
driver.close()
