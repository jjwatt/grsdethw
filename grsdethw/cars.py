from .element import BasePageElement, SelectPageElement
from .locators import HomePageLocators

class StockType(object):
    used = "Used Cars"
    new = "New Cars"

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
    
    @classmethod
    def fix_value(value):
        val = value
        if not isinstance(val, str):
            val = str(val)
        if val.startswith("$"):
            val = val[1:]
        if "," not in val:
            val = "{:,}".format(int(value))
        return "".join(["$", val]) 

#    def __set__(self, obj, value):
#        """Setter for PriceMaxElement."""
        # Make sure the price format is
        # "$50,000"
        # Accept ints or strs and use
        # str.format() to add the comma.
#        value = PriceMaxElement.fix_value(value)
        # super().__set__(obj, value) 

class RadiusElement(SelectPageElement):
    """Car is within X miles away."""
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

class SearchResultsPage(BasePage):
    """The results page after a search."""
    pass