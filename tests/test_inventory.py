import time
import pytest
from pages.inventory_page import InventoryPage


@pytest.mark.order(1)
def test_order_specific_product(driver,login):
    inv = InventoryPage(driver)
    inv.add_product_by_name("Sauce Labs Backpack")
    cart_count = inv.get_cart_count()
    assert cart_count == "1"

@pytest.mark.order(2)
def test_add_multiple_products(driver,login):
    inv = InventoryPage(driver)
    inv.add_multiple_products(["Sauce Labs Bolt T-Shirt", "Sauce Labs Bike Light"])
    cart_count = inv.get_cart_count()
    assert cart_count == "3"


@pytest.mark.order(3)
def test_sorting_price_low_to_high(driver,login):
    inv = InventoryPage(driver)
    inv.sort_by("Price (low to high)")
    prices = inv.get_all_product_prices()
    assert prices == sorted(prices), "Products not sorted by price low to high"

@pytest.mark.order(4)
def test_sorting_price_high_to_low(driver,login):
    inv = InventoryPage(driver)
    inv.sort_by("Price (high to low)")
    prices = inv.get_all_product_prices()
    assert prices == sorted(prices, reverse=True), " Products not sorted by price high to low"

@pytest.mark.order(5)
def test_sorting_assertion(driver,login):
    inv = InventoryPage(driver)
    inv.sort_by_name_ascending()
    names = inv.get_all_product_names()
    assert names == sorted(names), "Products not sorted A-Z"

