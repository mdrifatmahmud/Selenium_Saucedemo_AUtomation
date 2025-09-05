# conftest.py
import os
import shutil
import tempfile

import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from assets.login_assert import LoginAssert
from pages.login_page import LoginPage


@pytest.fixture(scope="session")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")  # Enable incognito mode
    chrome_options.add_argument("--start-maximized")  # Optional: start maximized

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )

    driver.get("https://www.saucedemo.com/")

    yield driver

    driver.quit()

@pytest.fixture(scope="session")
def login(driver):
    login = LoginPage(driver)
    a = LoginAssert(driver)
    login.login_without_exception_handle("standard_user", "secret_sauce")
    a.validate_url(driver.current_url)
    yield

def pytest_html_results_table_header(cells):
    cells.insert(2, "Description")

def pytest_html_results_table_row(report, cells):
    cells.insert(2, getattr(report, "description", "No description"))

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Get the standard report object
    outcome = yield
    report = outcome.get_result()

    # Attach the docstring as description
    if hasattr(item, "function"):
        report.description = str(item.function.__doc__) if item.function.__doc__ else "No description"
