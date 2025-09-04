from selenium.webdriver.common.by import By
import time

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_info_and_continue(self, first, last, zip_code):
        self.driver.find_element(By.ID, "first-name").send_keys(first)
        time.sleep(1)
        self.driver.find_element(By.ID, "last-name").send_keys(last)
        time.sleep(1)
        self.driver.find_element(By.ID, "postal-code").send_keys(zip_code)
        time.sleep(1)
        self.driver.find_element(By.ID, "continue").click()

    def cancel_order(self):
        time.sleep(1)
        self.driver.find_element(By.ID, "cancel").click()
        time.sleep(1)
