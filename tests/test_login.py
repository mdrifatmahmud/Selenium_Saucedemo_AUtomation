import time

import pytest
from selenium.common import WebDriverException
from selenium.webdriver.common.by import By

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

from assets.login_assert import LoginAssert



# @pytest.fixture(scope="session")
# def login(driver):
#     login = LoginPage(driver)
#     a = LoginAssert(driver)
#     login.login_without_exception_handle("standard_user", "secret_sauce")
#     a.validate_url(driver.current_url)
#     yield

