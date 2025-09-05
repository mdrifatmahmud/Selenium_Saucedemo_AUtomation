import time

import pytest
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.mark.order(1)
def test_cancel_order(driver,login):
    inv = InventoryPage(driver)
    inv.go_to_cart()
    cart = CartPage(driver)
    cart.click_checkout()
    checkout = CheckoutPage(driver)
    time.sleep(2)
    checkout.enter_info_and_continue("Test", "User", "12345")
    checkout.cancel_order()
    assert "inventory" in driver.current_url

