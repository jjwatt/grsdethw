from selenium.webdriver.support.ui import WebDriverWait, Select


class BasePageElement(object):
    "Base page element class for page objects."

    def __set__(self, obj, value):
        "Set text to value."
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element(*self.locator)
        )
        driver.find_element(*self.locator).clear()
        driver.find_element(*self.locator).send_keys(value)

    def __get__(self, obj, owner):
        """Gets the text of the specified object"""
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element(*self.locator)
        )
        element = driver.find_element(*self.locator)
        return element.get_attribute("value")


class SelectPageElement(BasePageElement):
    """Simple select page element class.

    Verified that this works on cars.locators select types.
    """

    def __set__(self, obj, value):
        "Set selection to value."
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element(*self.locator)
        )
        selector = Select(driver.find_element(*self.locator))
        selector.select_by_visible_text(value)
        # driver.find_element(self.locator).deselect_all()
        # driver.find_element(self.locator).select_by_value(value)
