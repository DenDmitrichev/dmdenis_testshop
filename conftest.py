import pytest
from selenium import webdriver

from pages.cart import CartPage
from pages.tables import Table
from pages.good import Good


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.implicitly_wait(5)
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture()
def table(driver):
    return Table(driver)


@pytest.fixture()
def goods(driver):
    return Good(driver)


@pytest.fixture()
def cart(driver):
    return CartPage(driver)
