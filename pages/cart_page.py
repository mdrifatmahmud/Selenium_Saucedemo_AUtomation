from selenium.webdriver.common.by import By
import time

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def click_checkout(self):
        time.sleep(1)
        self.driver.find_element(By.ID, "checkout").click()

