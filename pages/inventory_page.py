from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def add_product_by_name(self, name):
        items = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        time.sleep(1)
        for item in items:
            title = item.find_element(By.CLASS_NAME, "inventory_item_name").text
            if title == name:
                item.find_element(By.TAG_NAME, "button").click()
                break

    def add_multiple_products(self, names):
        time.sleep(1)
        items = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        for item in items:
            title = item.find_element(By.CLASS_NAME, "inventory_item_name").text
            if title in names:
                item.find_element(By.TAG_NAME, "button").click()

    def sort_by_name_ascending(self):
        time.sleep(1)
        Select(self.driver.find_element(By.CLASS_NAME, "product_sort_container")) \
            .select_by_visible_text("Name (A to Z)")
        time.sleep(1)

    def get_cart_count(self):
        time.sleep(1)
        return self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text

    def get_all_product_names(self):
        time.sleep(1)
        return [elem.text for elem in self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")]

    def go_to_cart(self):
        time.sleep(1)
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    def sort_by(self, option_text):
        time.sleep(1)
        from selenium.webdriver.support.ui import Select
        Select(self.driver.find_element(By.CLASS_NAME, "product_sort_container")) \
            .select_by_visible_text(option_text)

    def get_all_product_prices(self):
        time.sleep(1)
        prices = self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        return [float(p.text.replace("$", "")) for p in prices]

