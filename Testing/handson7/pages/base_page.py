from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        """
        Constructor

        Parameters:
            driver : Selenium WebDriver instance
        """
        self.driver = driver

    # --------------------------------------------------
    # Navigate to a URL
    # --------------------------------------------------

    def navigate_to(self, url):
        """
        Opens the given URL in the browser.
        """
        self.driver.get(url)

    # --------------------------------------------------
    # Get Page Title
    # --------------------------------------------------

    def get_title(self):
        """
        Returns the title of the current page.
        """
        return self.driver.title

    # --------------------------------------------------
    # Wait for Element
    # --------------------------------------------------

    def wait_for_element(self, locator, timeout=10):
        """
        Waits until the specified element is visible.

        Parameters:
            locator : Tuple (By.ID, "value")
            timeout : Maximum wait time (default = 10 sec)

        Returns:
            WebElement
        """
        wait = WebDriverWait(self.driver, timeout)

        return wait.until(
            EC.visibility_of_element_located(locator)
        )

    # --------------------------------------------------
    # Wait Until Clickable
    # --------------------------------------------------

    def wait_until_clickable(self, locator, timeout=10):
        """
        Waits until the element is clickable.
        """
        wait = WebDriverWait(self.driver, timeout)

        return wait.until(
            EC.element_to_be_clickable(locator)
        )

    # --------------------------------------------------
    # Click Element
    # --------------------------------------------------

    def click(self, locator):
        """
        Clicks an element.
        """
        self.wait_until_clickable(locator).click()

    # --------------------------------------------------
    # Enter Text
    # --------------------------------------------------

    def enter_text(self, locator, text):
        """
        Clears an input field and enters text.
        """
        element = self.wait_for_element(locator)

        element.clear()
        element.send_keys(text)

    # --------------------------------------------------
    # Get Element Text
    # --------------------------------------------------

    def get_text(self, locator):
        """
        Returns the text of an element.
        """
        return self.wait_for_element(locator).text