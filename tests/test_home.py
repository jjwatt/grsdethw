import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from grsdethw import cars


def determine_headless(fixture_name, config):
    """Provide option for headless runs."""
    opt = webdriver.firefox.options.Options()
    if config.getoption("--headless", None):
        opt.headless = True
    return opt


@pytest.fixture(scope="module")
def driver():
    return webdriver.Firefox()


@pytest.fixture(scope="module")
def home_page(driver):
    home = cars.Home(driver)
    # Use "yield" instead of return so that we can teardown the fixture
    # after all tests are done with it.
    # This allows re-entry from pytest, and then we close() the page.
    yield home
    # home.close()


# Scoping this as module means the fixture will be cached for all tests.
# Loading the home page is expensive, so this speeds up our tests.
# Setting autouse=True means we don't have to tell our tests to use it.
# All tests will just get it.
@pytest.fixture(scope="module", autouse=True)
def get_home_page(home_page):
    return home_page.get_home_page()


def test_load_home(home_page):
    assert home_page.title_looks_right(), "homepage title does not look right"


def test_select_make(home_page):
    home_page.make_element = "Honda"


def test_select_model(home_page):
    home_page.model_element = "Pilot"


def test_select_stock_type(home_page):
    home_page.stock_type_element = "Used Cars"


def test_set_zip_code(home_page):
    home_page.zip_code_element = "60008"


def test_select_price_max_element(home_page):
    # TODO(jjwatt): #1 Write a max_price(50000)
    home_page.price_max_element = "$50,000"


def test_select_radius_element(home_page):
    # These strings need to be exact.
    # TODO(jjwatt): Consider writing, e.g., miles_from(100)
    home_page.radius_element = "100 Miles from"


def test_search(home_page):
    home_page.click_search_button()
