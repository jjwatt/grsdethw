from selenium.webdriver.common import By

class HomePageLocators(object):
    """This class contains all Home Page locators for cars.com."""
    search_button = (By.XPATH, '//input[@value="Search"]')
    make = (By.XPATH, '//select[@name="makeId"]')
