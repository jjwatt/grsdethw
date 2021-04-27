from selenium.webdriver.common.by import By


class HomePageLocators(object):
    """This class contains all Home Page locators for cars.com."""

    stock_type = (By.XPATH, '//select[@name="stockType"]')
    search_button = (By.XPATH, '//input[@value="Search"]')
    make = (By.XPATH, '//select[@name="makeId"]')
    model = (By.XPATH, '//select[@name="modelId"]')
    zip_code = (By.XPATH, '//input[@name="zip"]')
    price_max = (By.XPATH, '//select[@name="priceMax"]')
    radius = (By.XPATH, '//select[@name="radius"]')
