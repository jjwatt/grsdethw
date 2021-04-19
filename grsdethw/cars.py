from selenium import webdriver
from selenium.webdriver.common.keys import keys

class BasePage(object):
    """Base page class."""
    def __init__(self, driver):
        self.driver = driver

class Home(BasePage):
    """Home page action methods."""
    def click_search_button(self):
        pass
