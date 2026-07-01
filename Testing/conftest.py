import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# --------------------------------------------------
# Browser Fixture
# --------------------------------------------------

@pytest.fixture(scope="function")
def driver(request):

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )

    driver.maximize_window()

    # Store driver so screenshot hook can access it
    request.node.driver = driver

    yield driver

    driver.quit()


# --------------------------------------------------
# Base URL Fixture
# --------------------------------------------------

@pytest.fixture(scope="session")
def base_url():
    return "https://www.lambdatest.com/selenium-playground/"


# --------------------------------------------------
# Screenshot on Failure
# --------------------------------------------------

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = getattr(item, "driver", None)

        if driver:
            screenshot_name = f"{item.name}_failure.png"
            driver.save_screenshot(screenshot_name)

            print(f"\nScreenshot saved as {screenshot_name}")