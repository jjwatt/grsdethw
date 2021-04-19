from selenium import webdriver
from selenium.webdriver.common.keys import keys

from element import BasePageElement
from locators import HomePageLocators


class BasePage(object):
    """Base page class."""

    def __init__(self, driver):
        self.driver = driver


class Home(BasePage):
    """Home page action methods."""

    def click_search_button(self):
        """Triggers the search."""
        element = self.driver.find_element(*HomePageLocators.search)
        element.click()
