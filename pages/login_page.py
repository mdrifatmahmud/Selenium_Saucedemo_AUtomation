import time

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        try:
            self.driver.find_element(By.ID, "user-name").send_keys(username)
            time.sleep(1)
            self.driver.find_element(By.ID, "password").send_keys(password)
            time.sleep(1)
            self.driver.find_element(By.ID, "login-button").click()
            time.sleep(1)
        except NoSuchElementException as e:
            print(f" Element not found during login: {e}")
            raise
        except TimeoutException as e:
            print(f" Timeout while interacting with login form: {e}")
            raise
        except Exception as e:
            print(f" Unexpected error during login: {e}")
            raise

    def get_error_text(self):
        try:
            return self.driver.find_element(*self.error_message).text
        except NoSuchElementException:
            return None

    def login_without_exception_handle(self, username, password):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        time.sleep(1)
        self.driver.find_element(By.ID, "password").send_keys(password)
        time.sleep(1)
        self.driver.find_element(By.ID, "login-button").click()
        time.sleep(1)