from .element import BasePageElement, SelectPageElement
from .locators import HomePageLocators


class StockTypeElement(SelectPageElement):
    """Class to select used or new."""

    locator = HomePageLocators.stock_type


class MakeElement(SelectPageElement):
    """Class to get or set the 'make' element on the page."""

    locator = HomePageLocators.make


class ModelElement(SelectPageElement):
    locator = HomePageLocators.model


class PriceMaxElement(SelectPageElement):
    locator = HomePageLocators.price_max


class RadiusElement(SelectPageElement):
    locator = HomePageLocators.radius


class ZipCodeElement(BasePageElement):
    """Class to access the Zip Code element on the page."""

    locator = HomePageLocators.zip_code


class BasePage(object):
    """Base page class."""

    def __init__(self, driver):
        self.driver = driver

    def close(self):
        self.driver.close()


class Home(BasePage):
    """Home page action methods."""

    stock_type_element = StockTypeElement()
    make_element = MakeElement()
    model_element = ModelElement()
    zip_code_element = ZipCodeElement()
    price_max_element = PriceMaxElement()
    radius_element = RadiusElement()

    def title_looks_right(self):
        """Verifies that the home page title looks right."""
        return "Cars" in self.driver.title

    def click_search_button(self):
        """Triggers the search."""
        element = self.driver.find_element(*HomePageLocators.search_button)
        element.click()

    def get_home_page(self):
        self.driver.get("http://www.cars.com")
