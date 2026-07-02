import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# -------------------------
# Driver Fixture
# -------------------------

@pytest.fixture(scope="function")
def driver():

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )

    driver.maximize_window()

    yield driver

    driver.quit()


# -------------------------
# Base URL Fixture
# -------------------------

@pytest.fixture(scope="session")
def base_url():

    return "https://www.lambdatest.com/selenium-playground/"