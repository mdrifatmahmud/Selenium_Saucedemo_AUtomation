import time

import pytest
from selenium.webdriver.common.by import By



@pytest.mark.order(2)
def test_logout(driver, login):
    driver.find_element(By.ID, "react-burger-menu-btn").click()
    time.sleep(1)
    driver.find_element(By.ID, "logout_sidebar_link").click()
    assert "saucedemo.com" in driver.current_url
